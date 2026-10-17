# Google Ads — Change Request CR-GA-0004 (Fitted Kitchens ad group)

**Status: approved 2026-10-17 and applied the same day; verified. Two differences from the CR are recorded in section 6 (keywords added in a second step; negatives at ad-group level, broad match). Review dates: 7 and 14 days after 2026-10-17 (2026-10-24, 2026-10-31).** Helen prepares sections 1–5; Minda completes 6 and applies in the Google Ads UI; Helen completes 7 at the review date.

**Request ID:** CR-GA-0004 · **Date:** 2026-10-17 · **Prepared by:** Helen
**Account:** AMFA Furniture Ltd (customer `1468068988`) · **Campaign:** Amfa - Bespoke Kitchens - Search (existing) · **Ad group:** NEW — "Fitted Kitchens"

## 1. Goal & success metric
- **What we're trying to achieve:** get the first impressions. The campaign has had **none in 18 days** (30 Sept – 17 Oct) and every setting I can read is healthy. This tests whether the problem is the narrow "bespoke" search market by adding the plan's second "Launch" service line — **fitted kitchens** — whose search terms are broader and more common (`CR-GA-0001`–`0003` and `Drafts/2026-10-09_Amfa_GoogleAds_Impressions-Plan_v1.md`).
- **Metric we'll judge it by:** impressions > 0 within 48h of applying; then impressions on **3 or more days in a row**; then clicks, click-through rate and the search-terms report. Conversions can't be judged yet — `form_submit` is still unconfirmed in GA4.
- **Review dates:** 7 days and 14 days after you apply it.

**Live state (read-only, 2026-10-17):** 1 campaign, `ENABLED`/`ELIGIBLE`/`SERVING`, Maximise Clicks, £25/day. 1 ad group with 13 phrase/broad keywords (7 `ELIGIBLE`, 6 `RARELY_SERVED`), all at 0 impressions. 1 RSA `APPROVED`. 11 campaign-level phrase negatives, 7 named locations, 50-mile radius around NE28, English, all devices. No restrictions found.

## 2. The exact change(s)

| # | Change type | Item | Match type | Suggested value | Rationale |
|---|---|---|---|---|---|
| 1 | add ad group | "Fitted Kitchens" in the existing campaign | n/a | no bid — Maximise Clicks | inherits the negatives, radius and £25/day budget |
| 2 | add keyword | `fitted kitchens Newcastle` | phrase | — | core local intent |
| 3 | add keyword | `fitted kitchens` | phrase | — | broader, more common; location targeting limits the area |
| 4 | add keyword | `fitted kitchen company Newcastle` | phrase | — | plan theme |
| 5 | add keyword | `new kitchen Newcastle` | phrase | — | wider buyer intent |
| 6 | add keyword | `kitchen company Newcastle` | phrase | — | wider buyer intent |
| 7 | add keyword | `new build kitchens Newcastle` | phrase | — | the site names new-build homes as a fitted-kitchen audience |
| 8 | add keyword | `affordable fitted kitchens North East` | phrase | — | plan theme (keyword only, not used as an ad claim) |
| 9 | add ad | one responsive search ad (section below) | n/a | final URL `https://amfa.uk/kitchens` | the only page covering fitted kitchens |
| 10 | add negatives (campaign level) | `flatpack`, `flat pack`, `cheap` | phrase | — | proposed — Minda to edit; the 11 from `CR-GA-0001` already apply |

No broad match at launch. Lesson from the Bespoke ad group: several phrases went `RARELY_SERVED`, including a broad one. If the same happens here, widen deliberately in a later request.

**Responsive Search Ad — headlines** (≤ 30 characters each, lengths checked by script)
1. Fitted Kitchens, Newcastle (26)
2. Kitchens From £2,000 (20)
3. Made-to-Measure Kitchens (24)
4. For New-Build Homes (19)
5. Apartments & New Builds (23)
6. Investment Property Kitchens (28)
7. Free Measuring Visit (20)
8. Up to 10-Year Warranty (22)
9. In-House Manufacturing (22)
10. 3D Design Before We Build (25)
11. Made in Newcastle (17)
12. Made in 3–8 Weeks (17)
13. Professionally Installed (24)
14. Get a Free Quote Today (22)
15. Over 100 Colour Options (23)

**Descriptions** (≤ 90 characters each)
1. Fitted kitchens from £2,000, made in-house in Newcastle. Free measuring visit, 50 miles. (88)
2. Made to fit your space and professionally installed. Up to 10-year warranty included. (85)
3. Choose from over 100 colour options. See your kitchen in 3D before we build. (76)
4. For apartments, new builds and investment properties. Get a free, no-obligation quote. (86)

**Sources:** live `https://amfa.uk/kitchens` (fetched 2026-10-17) — fitted kitchens "manufactured to fit the exact dimensions of your space and professionally installed", audiences (apartments, new-build homes, investment properties), "Prices from £2000", "3–8 weeks", warranty "up to 10 years", 3D visualisation before manufacturing, "over 100 ready-made colour options"; `/process` — free measuring visit within 50 miles; `Brand-and-Voice/Amfa-Furniture-Ltd.md`. No superlatives and no invented figures.

**Changes from the original plan's Fitted Kitchens copy (`Campaign-Plan_v1.md` §4):** dropped "Fitted in 3–8 Weeks" (the site's FAQ says production *and installation* take 6–10 weeks, so that would mislead — the 3–8 weeks is manufacturing only); dropped "Budget-Friendly, Built to Last" and "Quality Kitchens, Fair Prices" (subjective claims we can't substantiate); added "Over 100 Colour Options" (sourced from the live page).
**To confirm before launch:** "Prices from £2000" on the site is for kitchens generally, not fitted-only. Please confirm "from £2,000" is right for fitted kitchens.

## 3. Budget impact
- **Current daily budget:** £25.00 → **Proposed:** £25.00 (no change). The new ad group shares the campaign budget with the Bespoke ad group.
- **Expected spend change & why:** from £0 up to the cap, if the new terms find volume. Google decides how the £25 is split between the two ad groups.
- **Worst-case if it overspends:** Google may spend up to 2× the daily budget on a single day but not more than 30.4× in a month — about **£760/month** at £25/day. The £25/day cap still applies.

## 4. Reversibility (how to undo)
- Pause or remove the "Fitted Kitchens" ad group (Ad groups → select → Pause). Remove the added negatives (Keywords → Negative keywords). The Bespoke ad group, budget, radius and existing negatives are untouched.

## 5. Risk flags
- [ ] Broad match used (phrase only)
- [ ] Budget increase involved
- [x] New campaign / ads going live — a new ad group and ad, in an existing campaign
- [ ] Geo / audience change
- Notes:
  1. **Landing page:** `/kitchens` still has the unapplied MFC bracket fix (`Drafts/2026-09-24_Amfa_Copy-Fixes_v2.md`, item 7). Other copy and legal-page fixes (ledger rows 16/17/20) are also unapplied. Worth having the developer apply them before more traffic arrives.
  2. **Tracking:** `form_submit` unverified. A real test enquiry through the quote form is still outstanding.
  3. **Held in reserve, not part of this request:** switching to **Manual CPC** with real bids. It would change bidding for the whole campaign, and I have no keyword-planner data to suggest values. It only becomes relevant if Ad preview and diagnosis points to a bid or ad-rank reason.
  4. **Alongside:** `CR-GA-0003` (Wardrobes) is the other way to test different terms, and is still awaiting your section 6.

## 6. Approval (Minda)
- **Decision:** ☒ Approve as-is ☐ Approve with edits (below) ☐ Hold / reject
- **Edits / conditions:** none stated. Helen's open question — is "from £2,000" right for *fitted* kitchens? — was not answered separately; approval as-is is taken to accept the copy as written.
- **Approved by:** Minda (said "Approve as-is" in chat, recorded by Helen) · **Date:** 2026-10-17 · **Applied (where/when):** Google Ads UI, 2026-10-17, by Minda; verified read-only by Helen the same day. Items 1, 9 (ad group + RSA): as written — "Fitted Kitchens" in the existing campaign, 1 RSA `APPROVED`/`REVIEWED`, final URL `https://amfa.uk/kitchens`, all 15 headlines and 4 descriptions exactly as in the CR (Google's AI prefills and 3 AI-suggested sitelinks were cleared first; the descriptions have no trailing full stop). Items 2–8 (7 phrase keywords): applied as written but **not on the first save** — the first save created the ad group and ad with 0 keywords; Minda added them afterwards, all 7 present in Fitted Kitchens, `ENABLED`; 4 `ELIGIBLE`, 3 `RARELY_SERVED` (low search volume: `fitted kitchen company Newcastle`, `new build kitchens Newcastle`, `affordable fitted kitchens North East`), all `UNDER_REVIEW` at the time. Item 10 (negatives): applied **differently** — `cheap`, `flat pack`, `flatpack` were added at **ad-group level** on Fitted Kitchens, as **broad** match, not campaign-level phrase as the CR said. Effect: they apply to Fitted Kitchens only, not to the Bespoke ad group. Campaign still has its 11 phrase negatives. Budget unchanged (£25/day), locations and radius unchanged.

## 7. Post-apply check (Helen, at the review dates)
- **Result vs metric:** ____
- **Search-terms findings / new negatives:** ____
- **Next recommendation:** ____

---
_How to apply in the Ads UI: campaign → **Ad groups** → blue **+** → **New ad group** → name "Fitted Kitchens" → paste the 7 keywords, each in quotes for phrase match (e.g. `"fitted kitchens Newcastle"`) → create the responsive search ad with final URL `https://amfa.uk/kitchens`, pasting the 15 headlines and 4 descriptions → Save. Then **Keywords → Negative keywords** → add `flatpack`, `flat pack`, `cheap` at campaign level._
_Source: Eugene's Change Request template; lane per `Charter-Rules.md` Rule G._
