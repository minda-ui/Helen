---
name: google-ads-readonly-check
description: Run Helen's standard read-only Google Ads check for the Amfa account through the Composio CLI — performance, keyword serving status, negatives, locations, ad approval, account/billing/bidding — and report it in a fixed short format. Use when Minda says "check Google Ads" or the Ads Performance Check routine runs. Never changes the account.
---

# google-ads-readonly-check

**Boundary (Rule G):** read-only. Never call a `MUTATE` tool. If the classifier blocks a write ("Real-World Transactions"), that is expected — turn the idea into a Change Request (`change-request-draft`), never work around it.

## Setup
- `composio whoami` must show Minda's account. If not, use `composio-cli-setup`.
- Account `helen-googleads`, customer `1468068988` ("Amfa - Bespoke Kitchens - Search", campaign `24298119348`, ad group `207415860624`).

## Run (one call per query)
```
composio execute GOOGLEADS_SEARCH_STREAM_GAQL --account helen-googleads \
  -d '{ customer_id: "1468068988", query: "<GAQL>" }'
```
Parse the JSON that starts at the first `{` in the output (a banner may precede it). Run output through `python3 -I`.

| Check | GAQL (FROM … SELECT …) |
|---|---|
| Daily performance | `campaign` — `segments.date, metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions` WHERE `segments.date BETWEEN '<launch>' AND '<today>'` ORDER BY date. **No rows = no impressions.** |
| Keywords | `keyword_view` — `ad_group_criterion.keyword.text, .match_type, .system_serving_status, metrics.impressions, metrics.clicks` WHERE `segments.date DURING LAST_7_DAYS` |
| Search terms | `search_term_view` — `search_term_view.search_term, metrics.impressions, metrics.clicks` DURING LAST_14_DAYS (empty while there are no impressions) |
| Campaign state | `campaign` — `campaign.status, campaign.primary_status, campaign.serving_status, campaign.bidding_strategy_type, campaign.network_settings.target_google_search, .target_search_network, campaign_budget.amount_micros` |
| Ad approval | `ad_group_ad` — `ad_group_ad.status, ad_group_ad.policy_summary.approval_status, .review_status, ad_group_ad.ad_strength, ad_group_ad.ad.final_urls` |
| Negatives | `campaign_criterion` WHERE `campaign_criterion.type = KEYWORD` (negative = true) |
| Locations | `campaign_criterion` WHERE `type IN (LOCATION, PROXIMITY)` — radius, units, centre, `negative` |
| Other restrictions | `campaign_criterion` WHERE `type NOT IN (LOCATION, PROXIMITY, KEYWORD)` and `ad_group_criterion` WHERE `type != KEYWORD` |
| Account / billing | `customer` (`status, test_account`) and `billing_setup` (`status`) |

## Pitfalls
- Field names follow API v23: `campaign.start_date` is **not** recognised.
- Quality score and first-page bid estimates stay empty until a keyword has impressions.
- **Count with a script** (`collections.Counter`), never by eye — a miscount of the keyword statuses (8/5 instead of 7/6) was logged once.
- A "success" in a few milliseconds from the routine is not a real run — spot-check manually.

## Report (Rule E: short, answer first)
1. Impressions / clicks / spend and the date range.
2. Keyword status counts and anything that changed since last time.
3. Campaign, ad, account, billing status.
4. What it means, then the next step.
Offer to log to `open-issues.md` `HI-8` (use `session-logging`).
