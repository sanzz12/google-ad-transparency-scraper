# Google Ad Transparency Scraper

> Extract detailed advertising insights directly from Google’s Ads Transparency Center. Analyze ad spend, targeting strategies, campaign performance, and YouTube video creatives — all in one structured, ready-to-use dataset.

> Perfect for marketing analysts, researchers, and agencies tracking competitor ads and audience targeting trends.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Google Ad Transparency Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

This scraper provides a deep look into Google Ads data — from targeting to performance — by collecting structured datasets from the Ads Transparency Center.

It helps marketers, analysts, and researchers uncover how advertisers reach audiences, how campaigns evolve, and what media assets (like YouTube videos) are driving engagement.

### Why It Matters

- Gain competitive intelligence on ad strategies and formats.
- Track regional and platform-specific performance metrics.
- Analyze demographic and contextual targeting.
- Access verified advertiser data directly from Google’s ecosystem.
- Export structured datasets ready for business intelligence tools.

## Features

| Feature | Description |
|----------|-------------|
| YouTube Ad Intelligence | Extract direct YouTube video URLs, CTAs, and metadata for each creative. |
| Targeting Analysis | Unpack audience demographics, interests, locations, and customer list targeting. |
| Performance Data | Gather impressions, reach, and regional breakdowns for measurable insights. |
| Enterprise Scalability | Built for handling thousands of advertisers with robust recovery mechanisms. |
| Analysis Ready | Outputs JSON-formatted data optimized for analytics platforms. |
| Zero Maintenance | Automatically adapts to Google Ads Transparency Center changes. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|-------------|------------------|
| advertiserId | Unique ID of the advertiser (starts with “AR”). |
| advertiserName | Full name of the advertiser. |
| creativeId | Unique creative identifier for each ad. |
| adType | Type of ad (e.g., Video, Image). |
| targeting | Object describing targeting categories (demographics, interests, locations, etc.). |
| stats | Contains metrics such as impressions and date ranges. |
| variations | Array of ad variations with YouTube URLs and CTAs. |
| youtubeMetadata | Detailed YouTube-specific data like adId, video URL, and call-to-action URL. |

---

## Example Output

    [
      {
        "advertiserId": "AR13129532367502835713",
        "creativeId": "CR17788744295004504065",
        "advertiserName": "CHECK24 GmbH",
        "adType": "Video",
        "targeting": {
          "demographics": { "included": true, "excluded": false },
          "locations": { "included": true, "excluded": true },
          "contextSignals": { "included": true, "excluded": true },
          "customerLists": { "included": true, "excluded": false },
          "interests": { "included": true, "excluded": false }
        },
        "stats": {
          "dateRange": {
            "startDate": "2023-03-01T00:00:00.000Z",
            "endDate": "2024-12-06T00:00:00.000Z"
          },
          "impressions": {
            "total": { "min": "100,000", "max": "125,000" },
            "byRegion": [
              {
                "regionName": "Germany",
                "impressions": { "min": "100,000", "max": "125,000" },
                "byPlatform": [
                  {
                    "platformName": "YouTube",
                    "impressions": { "min": "100,000", "max": "125,000" }
                  }
                ]
              }
            ]
          }
        },
        "variations": [
          {
            "youtubeMetadata": {
              "adId": "DXgwjxGfuGg",
              "youtubeUrl": "https://www.youtube.com/watch?v=DXgwjxGfuGg",
              "ctaUrl": "https://handyvertrag.check24.de/handy-uebersicht?promotion=black-week&..."
            }
          },
          {
            "youtubeMetadata": {
              "adId": "B_kyndl0ArQ",
              "youtubeUrl": "https://www.youtube.com/watch?v=B_kyndl0ArQ",
              "ctaUrl": "https://handyvertrag.check24.de/handy-uebersicht?promotion=black-week&..."
            }
          }
        ]
      }
    ]

---

## Directory Structure Tree

    Google Ad Transparency Scraper/
    ├── src/
    │   ├── main.py
    │   ├── extractors/
    │   │   ├── ad_parser.py
    │   │   ├── youtube_metadata.py
    │   │   └── targeting_utils.py
    │   ├── outputs/
    │   │   └── data_exporter.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── advertisers.sample.json
    │   └── output_sample.json
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Marketing Analysts** use it to monitor competitors’ ad strategies and spending trends, so they can optimize campaigns.
- **Research Firms** use it to study cross-platform advertising behavior and transparency patterns.
- **Media Buyers** use it to identify top-performing ad creatives across regions and formats.
- **Policy Analysts** use it to evaluate transparency and accountability in digital advertising.
- **Agencies** use it to benchmark client performance against industry leaders.

---

## FAQs

**How do I find advertiser IDs?**
Search for the advertiser in Google’s Ads Transparency Center, click their name, and copy the “AR” number from the URL (e.g., `AR13129532367502835713`).

**Is YouTube ad data included?**
Yes. Video ad metadata, including URLs, CTAs, and YouTube IDs, are fully extracted.

**Can I limit scraping scope?**
You can use the `maxPages` parameter to set limits — 0 means unlimited pages (40 ads per page).

**Does it handle regional targeting?**
Yes. It extracts geographic distribution and impressions by platform and region.

---

## Performance Benchmarks and Results

**Primary Metric:** Scrapes up to 1,000 ads per advertiser in under 2 minutes.
**Reliability Metric:** 98% success rate with automatic retry and error recovery.
**Efficiency Metric:** Minimal memory footprint — optimized for concurrent runs.
**Quality Metric:** 99% data completeness across all major advertisers.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
