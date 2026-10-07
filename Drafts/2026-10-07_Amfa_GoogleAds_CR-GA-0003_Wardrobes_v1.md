# Google Ads — Change Request CR-GA-0003 (Wardrobes)

**Status: ready for Minda's review (section 6).** Nothing here has been applied. Helen prepares sections 1–5; Minda completes 6 and builds it in the Google Ads UI; Helen completes 7 at the review date.

**Request ID:** CR-GA-0003 · **Date:** 2026-10-07 · **Prepared by:** Helen
**Account:** AMFA Furniture Ltd (customer `1468068988`) · **Campaign:** NEW — "Amfa - Wardrobes - Search" · **Ad group:** "Fitted & Bespoke Wardrobes"

## 1. Goal & success metric
- **What we're trying to achieve:** a second Search campaign for wardrobes and bedroom storage — the plan's third "Launch" service line (`Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md` §2) — to find a service line with real search volume while Bespoke Kitchens is still at zero impressions.
- **Metric we'll judge it by:** impressions > 0 within 48h of going live; then clicks/week, search-terms quality, and enquiries. **Conversions can't be judged until `form_submit` is confirmed in GA4** (a real test enquiry through the quote form is still outstanding).
- **Review dates:** 7 days and 14 days after go-live (search terms, then full review).

## 2. The exact change(s)

**A. Structure — pick one:**
- **Option 1 (as requested): new separate campaign** with its own budget, settings and reporting. Cleaner to read; needs its own negatives, location and conversion settings.
- **Option 2: new ad group "Wardrobes" inside the existing campaign.** Matches the original plan (one campaign, ad groups by service line); inherits the 11 negatives, the 50-mile radius and the £25/day budget. Simpler, but wardrobes and kitchens then compete for one budget and share one set of reports.

The rest of this request applies to either option.

**B. Campaign settings (Option 1)**
| Setting | Value |
|---|---|
| Type / goal | Search · leads (same goal as the Kitchens campaign; review "Leads from messages" vs website form once conversion data exists — flagged in `HI-8`) |
| Networks | Google Search Network only. **Search partners off** (small budget, tighter traffic) — differs from Kitchens, which has them on |
| Locations | 50-mile radius around NE28 6HA, plus the same 7 named locations as Kitchens (as per `CR-GA-0002`). Location option: **Presence** recommended (your decision on `CR-GA-0002` item 2 should apply here too) |
| Bidding | Maximise Clicks to start, with a **maximum CPC limit** set by Minda (no value suggested — no keyword-planner data). Switch to Maximise Conversions once `form_submit` is imported |
| Language / AI Max | English · AI Max **off**, automatically created assets **off** (so only reviewed copy runs) |
| Final URL | `https://amfa.uk/wardrobe-bedroom` |

**C. Keywords (phrase match; themes from the plan, not verified volumes — validate in Keyword Planner before launch)**
| Keyword | Match type | Rationale |
|---|---|---|
| `fitted wardrobes Newcastle` | phrase | core local intent |
| `bespoke wardrobes Newcastle` | phrase | premium positioning |
| `walk-in wardrobe design` | phrase | walk-in is a named service |
| `walk-in closet Newcastle` | phrase | plan theme (walk-in closet installation) |
| `sliding door wardrobes Newcastle` | phrase | named service |
| `made to measure wardrobes` | phrase | in-house, made-to-measure |
| `fitted bedroom furniture Newcastle` | phrase | plan theme |
| `bespoke bedroom furniture` | phrase | plan theme |
No broad match on launch. Lesson from Kitchens: several narrow phrases went `RARELY_SERVED`; if the same happens here, widen deliberately in a later request rather than at launch.

**D. Negative keywords (campaign level, phrase — proposals; Minda to edit)**
Same as `CR-GA-0001`: `jobs`, `job`, `careers`, `salary`, `apprenticeship`, `diy`, `free`, `second hand`, `used`, `ikea`, `b&q`. Wardrobe-specific additions: `flatpack`, `flat pack`, `cheap`, `repair`, `rental`. **Tip:** create one shared negative keyword list (Tools → Shared library → Negative keyword lists) and apply it to both campaigns. Apply negatives **before** the campaign goes live.

**E. Responsive Search Ad** (every line checked against the 30 / 90 character limits)
Headlines:
1. Fitted Wardrobes, Newcastle (27)
2. Bespoke Wardrobes & Closets (27)
3. Made-to-Measure Wardrobes (25)
4. Walk-In Wardrobe Design (23)
5. Sliding Door Wardrobes (22)
6. Wardrobes From £2,000 (21)
7. Free Measuring Visit (20)
8. Up to 10-Year Warranty (22)
9. In-House Manufacturing (22)
10. 3D Design Before We Build (25)
11. Made in Newcastle (17)
12. Made in 4–8 Weeks (17)
13. Fitted Bedroom Furniture (24)
14. Get a Free Quote Today (22)
15. Designed for Your Space (23)

Descriptions:
1. Wardrobes designed and made in-house in Newcastle. Up to 10-year warranty included. (83)
2. Fitted, sliding-door and walk-in wardrobes from £2,000. Free measuring visit, 50 miles. (87)
3. See your wardrobe in 3D before we build. Made in 4–8 weeks, then professionally installed. (90)
4. Made to the exact dimensions of your room. Get a free, no-obligation quote today. (81)

**Sources for every claim** (no superlatives, no invented figures): live `/wardrobe-bedroom` page (fetched 2026-10-07) — "Prices from £2000", production "4–8 weeks … followed by professional installation", warranty "up to 10 years"; `/process` — free measuring visit "within 50 miles", 3D visualisation, in-house team; `Brand-and-Voice/Amfa-Furniture-Ltd.md`. Check "From £2,000" is current before launch — the brand file has no wardrobe price floor yet.

**F. Extensions:** sitelinks — Wardrobe & Bedroom Storage, Portfolio, Process, Get a Free Quote · call 01916052945 · location Unit 30, Point Pleasant Industrial Estate, Newcastle Upon Tyne NE28 6HA · callouts: In-House Manufacturing, Up to 10-Year Warranty, Free Measuring Visit · message asset (WhatsApp) +44 7392 592864, starter text "Hi! Interested in a fitted wardrobe? Send us a message and we'll get back to you with a free quote." (99/140).

## 3. Budget impact
- **Current daily budget:** £25.00 (Kitchens) → **Proposed:** Minda decides — options below. Helen does not set spend.
| Option | Kitchens | Wardrobes | Account total | Max per month* |
|---|---|---|---|---|
| Split | £15 | £10 | £25 (no increase) | ≈ £760 |
| Add on top | £25 | £10 | £35 (**+£10/day**) | ≈ £1,064 |
| Add on top | £25 | £15 | £40 (**+£15/day**) | ≈ £1,216 |
\*Google may spend up to 2× the daily budget on one day but not more than 30.4× the daily budget in a month. The daily cap is the limit that applies. Amounts are illustrations for your decision, not recommendations — neither campaign has any performance data yet.
- **Expected spend change & why:** from £0 on this campaign to up to its daily budget, if the keywords find volume. Kitchens has spent £0 so far.
- **Worst-case if it overspends:** the monthly maximum in the table for the option you choose.

## 4. Reversibility (how to undo)
- **Pause the campaign** (Campaigns → select → Pause), or remove it. No effect on the Kitchens campaign. Budget returns to the previous figure (if you split, restore Kitchens to £25). Under Option 2, pause or remove the ad group instead.

## 5. Risk flags
- [ ] Broad match used (phrase only)
- [x] Budget increase involved — only if you choose "Add on top"
- [x] New campaign / ads going live
- [x] Geo / audience change — new campaign needs its own location settings
- Notes:
  1. **Landing page:** `/wardrobe-bedroom` still has the unapplied MFC bracket fix (copy-fixes v2, item 7: `High-quality MFC (Melamine Faced Chipboard` is missing its closing bracket). The site's legal-page placeholder fixes and other copy fixes (ledger rows 16/17/20) are also unapplied. Worth having the developer apply them before paying for traffic.
  2. **Conversion tracking:** `form_submit` unverified in GA4. Do a real test enquiry first so wardrobes can be judged on enquiries, not just clicks.
  3. **Timing:** you may prefer to wait for the Kitchens read-outs (search terms Oct 9, locations Oct 10, full review Oct 13–14) before committing a budget.

## 6. Approval (Minda)
- **Decision:** ☐ Approve as-is ☐ Approve with edits (below) ☐ Hold / reject
- **Structure:** ☐ Option 1 separate campaign ☐ Option 2 ad group · **Budget:** ☐ Split ☐ Add on top £__/day ☐ Other £__/day
- **Edits / conditions:** ____
- **Approved by:** ____ · **Date:** ____ · **Applied (where/when):** ____

## 7. Post-apply check (Helen, at the review dates)
- **Result vs metric:** ____
- **Search-terms findings / new negatives:** ____
- **Next recommendation:** ____

---
_Source: Eugene's Change Request template; lane per `Charter-Rules.md` Rule G. Campaign plan: `Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md`._
