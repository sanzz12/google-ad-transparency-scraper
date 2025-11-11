thonfrom __future__ import annotations

import logging
from datetime import datetime
from typing import Any, Dict, List

from .targeting_utils import normalize_targeting
from .youtube_metadata import ensure_youtube_metadata

LOGGER = logging.getLogger("google_ad_transparency_scraper.ad_parser")

def _safe_date(value: Any) -> str:
    """
    Best-effort conversion of an arbitrary value into an ISO 8601 string.
    If parsing fails, the value is returned as-is if it looks like a string,
    otherwise a fallback date is provided.
    """
    if isinstance(value, str) and value:
        try:
            # Try to parse a few common formats
            for fmt in ("%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"):
                try:
                    return datetime.strptime(value, fmt).isoformat() + "Z"
                except ValueError:
                    continue
            # If parsing failed but it's a string, just return it untouched
            return value
        except Exception:  # noqa: BLE001
            return "1970-01-01T00:00:00.000Z"

    return "1970-01-01T00:00:00.000Z"

def _normalize_impression_bucket(bucket: Dict[str, Any]) -> Dict[str, str]:
    """
    Normalizes an impressions bucket into a dict with 'min' and 'max' string values.
    """
    if not isinstance(bucket, dict):
        return {"min": "0", "max": "0"}

    def _to_str(v: Any) -> str:
        if v is None:
            return "0"
        if isinstance(v, (int, float)):
            return f"{int(v):,}"
        return str(v)

    min_val = _to_str(bucket.get("min"))
    max_val = _to_str(bucket.get("max"))
    return {"min": min_val, "max": max_val}

def _normalize_stats(stats: Dict[str, Any] | None) -> Dict[str, Any]:
    if stats is None:
        return {
            "dateRange": {
                "startDate": "1970-01-01T00:00:00.000Z",
                "endDate": "1970-01-01T00:00:00.000Z",
            },
            "impressions": {
                "total": {"min": "0", "max": "0"},
                "byRegion": [],
            },
        }

    date_range = stats.get("dateRange") or {}
    start_date = _safe_date(date_range.get("startDate"))
    end_date = _safe_date(date_range.get("endDate"))

    impressions = stats.get("impressions") or {}
    total_bucket = _normalize_impression_bucket(impressions.get("total") or {})

    by_region_raw = impressions.get("byRegion") or []
    by_region: List[Dict[str, Any]] = []
    if isinstance(by_region_raw, list):
        for region in by_region_raw:
            if not isinstance(region, dict):
                continue
            region_name = region.get("regionName") or "Unknown"
            region_impressions = _normalize_impression_bucket(region.get("impressions") or {})
            by_platform_raw = region.get("byPlatform") or []
            by_platform: List[Dict[str, Any]] = []
            if isinstance(by_platform_raw, list):
                for platform in by_platform_raw:
                    if not isinstance(platform, dict):
                        continue
                    platform_name = platform.get("platformName") or "Unknown"
                    platform_impressions = _normalize_impression_bucket(
                        platform.get("impressions") or {}
                    )
                    by_platform.append(
                        {
                            "platformName": platform_name,
                            "impressions": platform_impressions,
                        }
                    )
            by_region.append(
                {
                    "regionName": region_name,
                    "impressions": region_impressions,
                    "byPlatform": by_platform,
                }
            )

    return {
        "dateRange": {
            "startDate": start_date,
            "endDate": end_date,
        },
        "impressions": {
            "total": total_bucket,
            "byRegion": by_region,
        },
    }

def _normalize_variations(raw_variations: Any) -> List[Dict[str, Any]]:
    result: List[Dict[str, Any]] = []
    if not isinstance(raw_variations, list):
        raw_variations = []

    for variation in raw_variations:
        if not isinstance(variation, dict):
            continue
        try:
            normalized = ensure_youtube_metadata(variation)
            result.append(normalized)
        except Exception as exc:  # noqa: BLE001
            LOGGER.warning("Failed to normalize variation %r: %s", variation, exc)
    return result

def parse_advertiser_ads(
    advertiser_id: str,
    advertiser_name: str,
    raw_ads: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """
    Parse a list of raw ad records into the normalized schema described in the README.

    Each resulting item looks like:

    {
      "advertiserId": "...",
      "creativeId": "...",
      "advertiserName": "...",
      "adType": "...",
      "targeting": {...},
      "stats": {...},
      "variations": [...]
    }
    """
    normalized: List[Dict[str, Any]] = []

    if not isinstance(raw_ads, list):
        LOGGER.warning(
            "Expected raw_ads to be a list for advertiser %s, got %r",
            advertiser_id,
            type(raw_ads),
        )
        return normalized

    for raw in raw_ads:
        if not isinstance(raw, dict):
            LOGGER.debug("Skipping non-dict ad entry: %r", raw)
            continue

        creative_id = raw.get("creativeId") or raw.get("id") or ""
        ad_type = raw.get("adType") or raw.get("type") or "Unknown"

        targeting_raw = raw.get("targeting")
        targeting = normalize_targeting(targeting_raw)

        stats_raw = raw.get("stats")
        stats = _normalize_stats(stats_raw)

        variations_raw = raw.get("variations")
        variations = _normalize_variations(variations_raw)

        ad_record: Dict[str, Any] = {
            "advertiserId": advertiser_id,
            "creativeId": creative_id,
            "advertiserName": advertiser_name,
            "adType": ad_type,
            "targeting": targeting,
            "stats": stats,
            "variations": variations,
        }

        normalized.append(ad_record)

    return normalized