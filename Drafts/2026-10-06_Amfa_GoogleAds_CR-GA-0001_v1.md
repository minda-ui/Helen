# Google Ads — Change Request CR-GA-0001

**Status: approved 2026-10-07. Negatives applied and verified; broad keywords differ from §2 (see section 6).** Helen prepares sections 1–5; Minda completes 6 and applies in the Google Ads UI; Helen completes 7 at the review date.

**Request ID:** CR-GA-0001 · **Date:** 2026-10-06 · **Prepared by:** Helen
**Account:** AMFA Furniture Ltd (customer `1468068988`) · **Campaign:** Amfa - Bespoke Kitchens - Search · **Ad group:** the single Bespoke Kitchens ad group (id `207415860624`)

## 1. Goal & success metric
- **What we're trying to achieve:** first impressions and clicks. The campaign has had none since launch (30 Sept).
- **Metric we'll judge it by:** impressions > 0 within 48h of applying; then clicks/week and search-terms quality. **Not conversions yet** — `form_submit` has not been confirmed in GA4 (open since 2026-09-29), so CPA can't be judged.
- **Review dates:** mid-week check **2026-10-09** (search terms), full review **2026-10-13**.

**Evidence (read-only, 2026-10-06):** 0 impressions, clicks and spend over 7 days; account, billing, campaign, ad and location targeting all healthy. 10 phrase-match keywords, all `ENABLED`: 5 `ELIGIBLE`, 5 `RARELY_SERVED`. No impression-share rows at all, so Google isn't entering auctions. Most likely cause: thin search volume for exact phrases in a 7-town area. Broad match widens the pool. Source: `open-issues.md` `HI-8`.

## 2. The exact change(s)
| # | Change type | Item | Match type | Suggested value | Rationale |
|---|---|---|---|---|---|
| 1 | add keyword | `bespoke kitchens` | broad | no bid — campaign uses Maximise Clicks (see §3 note) | strongest eligible phrase; widest reach |
| 2 | add keyword | `kitchen designer Newcastle` | broad | as above | local, high-intent; phrase version is eligible but silent |
| 3 | add negative keywords (campaign level) | list below | phrase | n/a | broad match needs them first |

**Negatives to add (proposed — Minda to edit):** `jobs`, `job`, `careers`, `salary`, `apprenticeship`, `diy`, `free`, `second hand`, `used`, `ikea`, `b&q`. Competitor names (`ikea`, `b&q`) are a judgement call — drop if you'd rather not exclude them. **Apply the negatives before or together with the broad keywords, never after.**

## 3. Budget impact
- **Current daily budget:** £25.00 → **Proposed:** £25.00 (no change)
- **Expected spend change & why:** from £0 to up to the daily budget, if broad match finds volume. That is the point of the change.
- **Worst-case if it overspends:** Google may spend up to 2× the daily budget on a single day but not more than 30.4× the daily budget in a month — about **£760/month** at £25/day. The £25/day cap is the limit that applies.
- **Note for Minda:** Maximise Clicks has no CPC ceiling set. Optional safeguard: set a maximum CPC limit on the bidding strategy. Helen has no keyword-planner data, so no value is suggested; choose one if you want it.

## 4. Reversibility (how to undo)
- Pause or remove the two broad keywords (Keywords → select → Pause). Pause or remove the added negatives (Keywords → Negative keywords). Budget is untouched. The existing 10 phrase keywords are unchanged.

## 5. Risk flags
- [x] Broad match used → negatives (§2), cap (£25/day) and first-week search-terms review (2026-10-09) attached
- [ ] Budget increase involved
- [ ] New campaign / ads going live
- [ ] Geo / audience change
- Notes: ads still point at `amfa.uk`, where the 7 copy fixes (ledger rows 16/17) and legal-page placeholder fixes (row 20) are unapplied. Worth fixing before paying for more traffic.

## 6. Approval (Minda)
- **Decision:** ☒ Approve as-is ☐ Approve with edits (below) ☐ Hold / reject
- **Edits / conditions:** ____
- **Approved by:** Minda (said "Approve as-is" in chat, recorded by Helen) · **Date:** 2026-10-07 · **Applied (where/when):** Item 3 (negatives) — applied by Minda in the Google Ads UI, 2026-10-07; verified read-only by Helen the same day: all 11 present, campaign level, phrase match, `ENABLED` (`jobs`, `job`, `careers`, `salary`, `apprenticeship`, `diy`, `free`, `second hand`, `used`, `ikea`, `b&q`); none at ad-group level. Items 1–2 (broad `bespoke kitchens`, `kitchen designer Newcastle`) — not applied as written; broad `bespoke kitchens newcastle` and `handmade kitchens newcastle` were added by Minda instead (seen 2026-10-07)

## 7. Post-apply check (Helen, at the review date)
- **Result vs metric:** ____
- **Search-terms findings / new negatives:** ____
- **Next recommendation:** ____

---
_Source: Eugene's Change Request template (`Research/2026-10-06_GoogleAds_Change-Request-Template_from-Eugene.md`); lane per `Charter-Rules.md` Rule G._
