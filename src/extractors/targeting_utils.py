thonfrom __future__ import annotations

from typing import Any, Dict

def _bool_or_false(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"1", "true", "yes", "y"}:
            return True
    return False

def _normalize_inclusion_block(block: Any) -> Dict[str, bool]:
    """
    Normalize any incoming value into a simple {included: bool, excluded: bool} block.
    """
    if isinstance(block, dict):
        return {
            "included": _bool_or_false(block.get("included")),
            "excluded": _bool_or_false(block.get("excluded")),
        }

    # If block is a boolean or a non-empty container, treat it as "included"
    included = _bool_or_false(block)
    return {
        "included": included,
        "excluded": False,
    }

def normalize_targeting(targeting: Any) -> Dict[str, Any]:
    """
    Convert various raw targeting forms into a consistent structure:

    {
      "demographics": { "included": bool, "excluded": bool },
      "locations": { "included": bool, "excluded": bool },
      "contextSignals": { "included": bool, "excluded": bool },
      "customerLists": { "included": bool, "excluded": bool },
      "interests": { "included": bool, "excluded": bool }
    }
    """
    targeting = targeting or {}

    if not isinstance(targeting, dict):
        targeting = {}

    demographics_block = targeting.get("demographics")
    locations_block = targeting.get("locations")
    context_block = (
        targeting.get("contextSignals")
        or targeting.get("context")
        or targeting.get("topics")
    )
    customer_lists_block = (
        targeting.get("customerLists")
        or targeting.get("customerList")
        or targeting.get("crmLists")
    )
    interests_block = targeting.get("interests") or targeting.get("audiences")

    return {
        "demographics": _normalize_inclusion_block(demographics_block),
        "locations": _normalize_inclusion_block(locations_block),
        "contextSignals": _normalize_inclusion_block(context_block),
        "customerLists": _normalize_inclusion_block(customer_lists_block),
        "interests": _normalize_inclusion_block(interests_block),
    }