# Google Ads — Change Request CR-GA-0002

**Status: radius applied by Minda 2026-10-07 and verified (50 miles). Section 6 sign-off and the optional Presence setting still open.** Helen prepares sections 1–5; Minda completes 6 and applies in the Google Ads UI; Helen completes 7 at the review date.

**Request ID:** CR-GA-0002 · **Date:** 2026-10-07 · **Prepared by:** Helen
**Account:** AMFA Furniture Ltd (customer `1468068988`) · **Campaign:** Amfa - Bespoke Kitchens - Search · **Ad group:** n/a (campaign-level setting)

## 1. Goal & success metric
- **What we're trying to achieve:** widen the geography to a **radius of NE28 6HA** (Minda's brief, 2026-10-07: 40 miles, changed to **50 miles** the same day, matching the original plan), so the campaign can reach more searchers. It has had zero impressions since launch.
- **Metric we'll judge it by:** impressions > 0 within 48h of applying; then clicks/week, and the share of clicks coming from outside the old 7 locations. Conversions can't be judged yet — `form_submit` is still unconfirmed in GA4.
- **Review dates:** location report check **2026-10-10**, full review **2026-10-14**.

**Current setup (read-only, 2026-10-07):** 7 named locations, all positive and `ENABLED`: Durham, Gateshead, Newcastle upon Tyne, North Shields, Northumberland, South Shields, Sunderland. No radius targets. Location option: **Presence or interest** (people in the area *or* showing interest in it). The original plan (`Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md`) used a 50-mile Newcastle radius to match the confirmed measuring-visit area, so **40 miles is a change from that plan** — please confirm it replaces it.

## 2. The exact change(s)
| # | Change type | Item | Match type | Suggested value | Rationale |
|---|---|---|---|---|---|
| 1 | add location (radius) | centre `NE28 6HA`, radius | n/a | **50 miles** (briefed as 40, changed same day) | matches the original 50-mile plan; overlaps and extends the 7 named areas |
| 2 | location option (optional) | Presence or interest → **Presence** | n/a | Presence: people in or regularly in the area | stops ads showing to people outside the radius who only search *about* it |

**How the 7 named locations are handled — pick one:**
- **A (recommended, matches "add"):** keep all 7 and add the radius. Nothing is removed. Northumberland stays in full, including areas beyond 40 miles.
- **B:** replace the 7 with the radius alone. A strict 40 miles, but it drops the far-north part of Northumberland that lies outside it.

**Negatives:** none needed for this change (the 11 from CR-GA-0001 stay in place).

## 3. Budget impact
- **Current daily budget:** £25.00 → **Proposed:** £25.00 (no change)
- **Expected spend change & why:** none from the setting itself. The same £25/day is spread over a larger area, so spend may rise toward the cap only if the wider area produces more searches.
- **Worst-case if it overspends:** Google may spend up to 2× the daily budget on a single day but not more than 30.4× in a month — about £760/month at £25/day. The £25/day cap still applies.

## 4. Reversibility (how to undo)
- Remove the radius target (Locations → select it → Remove). Set the location option back to Presence or interest. The 7 named locations are untouched under option A.

## 5. Risk flags
- [ ] Broad match used
- [ ] Budget increase involved
- [ ] New campaign / ads going live
- [x] Geo / audience change → first-week location report review attached (2026-10-10)
- Notes: (1) The service-area wording on `amfa.uk` and in `Brand-and-Voice/Amfa-Furniture-Ltd.md` should match the final radius before more paid traffic lands there; Helen will check once you confirm 40 miles. (2) Radius is measured from the postcode point, so towns near the edge may be partly outside it. (3) Ads still point at `amfa.uk`, where the copy fixes (ledger rows 16/17) and legal placeholder fixes (row 20) are unapplied.

## 6. Approval (Minda)
- **Decision:** ☐ Approve as-is ☐ Approve with edits (below) ☐ Hold / reject
- **Option for the 7 named locations:** ☐ A keep ☐ B replace · **Presence-only (item 2):** ☐ yes ☐ no
- **Edits / conditions:** ____
- **Approved by:** Minda (applied in the Ads UI; formal section-6 ticks not given) · **Date:** 2026-10-07 · **Applied (where/when):** Item 1 — Google Ads UI, 2026-10-07; verified read-only by Helen the same day: 1 `PROXIMITY` target, `ENABLED`, positive, **50 miles**, centred at 55.001125, -1.532803 (address field reads "Wallsend NE28", the postcode district, not the full NE28 6HA — immaterial at 50 miles). The 7 named locations remain (option A). Item 2 (Presence only) — **not applied**: location option is still "Presence or interest".

## 7. Post-apply check (Helen, at the review date)
- **Result vs metric:** ____
- **Location report findings:** ____
- **Next recommendation:** ____

---
_How to apply in the Ads UI: campaign → **Locations** (left menu) → pencil icon **Edit locations** → **Advanced search** → **Radius targeting** → type `NE28 6HA`, set **40 mi**, choose the postcode result → **Add** → **Save**. For item 2: Locations → **Location options** → **Presence**._
_Source: Eugene's Change Request template; lane per `Charter-Rules.md` Rule G._
