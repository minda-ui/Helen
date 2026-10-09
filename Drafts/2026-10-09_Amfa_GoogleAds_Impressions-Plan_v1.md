# Amfa Google Ads — plan to start getting impressions

**Company:** Amfa Furniture Ltd · **Date:** 2026-10-09 · **Prepared by:** Helen · **Status:** ready for Minda's review
**Lane:** Rule G — Helen reads and prepares; Minda applies every live change. Nothing here has been changed in the account. Source of the evidence: read-only checks 2026-10-05 → 2026-10-09 (`HI-8`).

## 1. Where we are
Campaign "Amfa - Bespoke Kitchens - Search", live since 30 Sept: **0 impressions, 0 clicks, £0 in 10 days.**

**Ruled out (checked directly, not assumed):**
| Area | Result |
|---|---|
| Account / billing | `ENABLED`, real account, billing `APPROVED` |
| Campaign | `ENABLED`, `SERVING`, primary status `ELIGIBLE`, budget £25/day |
| Ad | 1 RSA `APPROVED`/`REVIEWED`, no policy flags, ad strength Average |
| Keywords | 13 `ENABLED`: 7 `ELIGIBLE`, 6 `RARELY_SERVED`; 2 already broad match |
| Targeting | 7 named locations + 50-mile radius (NE28), English, desktop/mobile/tablet all on, **no** schedule, audience, age or gender restrictions, no location exclusions |
| Negatives | 11 campaign-level phrase negatives — none look like they'd block these keywords |
| Networks | Search + Search partners on |
| Bidding | Maximise Clicks, status `ENABLED`, no CPC ceiling |
| Website | `amfa.uk` loads for Google's ad crawler user-agent (HTTP 200); `robots.txt` blocks only Tilda internals |

**What's odd:** with 7 `ELIGIBLE` keywords, two of them broad, a 50-mile area and 10 days, you would normally see *a few* impressions even if volume is low. **Zero, with no impression-share data at all, means Google isn't entering auctions** — not losing them. "Thin volume" is plausible but is not proven. No keyword has a quality score or a first-page bid estimate yet, because those only appear after impressions.

**One thing noted, probably harmless:** every keyword shows an effective CPC bid of £0.01 (the ad-group default). With Maximise Clicks that bid is normally ignored, but I can't confirm that from here — step 1 below will.

## 2. The plan

### Step 1 — Find out why the ad isn't showing (Minda, today, ~5 minutes) ★ most useful
Google's **Ad preview and diagnosis** tool states the exact reason an ad isn't showing.
1. Ads UI → **Tools** → **Troubleshoot** → **Ad preview and diagnosis**.
2. Enter search term `kitchens Newcastle`; location **Newcastle upon Tyne** (or `NE28 6HA`); language English; device Desktop; domain `google.co.uk`. Click **Search**.
3. Repeat for `bespoke kitchens`.
4. Send me the message it shows (text or screenshot) — it either shows the ad or gives a reason.

### Step 2 — Check real search volume (Minda, today, ~10 minutes)
Tools → **Keyword Planner** → **Get search volume and forecasts**. Paste the 13 Kitchens keywords plus the 8 Wardrobe keywords from `CR-GA-0003`. Set location to the 50-mile radius around NE28 (or Newcastle upon Tyne). Send me the monthly searches per keyword. This tells us whether volume is the problem and which service line has more.

### Step 3 — Confirm two settings by eye (Minda, ~3 minutes)
Campaign → **Settings**: (a) bid strategy reads **Maximise clicks** with **no** "maximum CPC bid limit" set; (b) the **Goals** section: "Leads from messages" — note it for later, no change. If (a) shows anything else, tell me.

### Step 4 — Act on what steps 1–3 show (Helen drafts a CR; Minda applies)
| If the diagnosis / planner shows… | Then the lever is… | Change request |
|---|---|---|
| Ad not eligible / a policy or account reason | Fix that reason first | new CR for the specific fix |
| Bid or ad-rank reason | Switch the ad group to **Manual CPC** with a real per-keyword bid taken from Keyword Planner's page-one estimates — forces auction entry and gives control; cap stays at £25/day | CR-GA-0004 |
| Search volume low for the Kitchens terms | **Widen the product range**: build the **Fitted Kitchens ad group** already planned (ad copy written and character-checked in the campaign plan) — `fitted kitchens Newcastle` and similar are broader, higher-volume terms | CR-GA-0004 |
| A different service line has clearly more volume | Go live with **Wardrobes** (`CR-GA-0003`, ready) | CR-GA-0003 |
| Diagnosis shows the ad *would* show | Volume is the cause. Keep the live setup, add the broader terms above, and give it 7 more days | CR-GA-0004 |

### Step 5 — Smaller supporting changes (any time)
- Send the Kitchens ad to **`/kitchens`**, not the homepage (relevance and quality score once traffic arrives). CR-GA-0005.
- Add a second RSA with different wording, so Google has more combinations (ad strength is Average). CR-GA-0005.

### Beyond Search ads (not for now, listed so they aren't forgotten)
- **Google Business Profile** for the Newcastle showroom — free local visibility for searches like "kitchen showroom Newcastle". In my scope; I can draft the listing content for you to publish.
- **Microsoft/Bing Advertising** — scope added 2026-10-06, nothing built. Uses the same Change Request pattern.
- **Performance Max / Demand Gen** — only worth discussing if Search volume proves genuinely thin. Not planned.

## 3. Timeline
| When | What | Who |
|---|---|---|
| Fri 9 Oct | Steps 1–3 | Minda |
| Fri 9 / Sat 10 Oct | Read your results, draft CR-GA-0004 (and 0005) | Helen |
| Mon 12 Oct | Apply the chosen CR in the Ads UI | Minda |
| Tue 13 Oct | Read-only check: any impressions? | Helen |
| Wed 14 – Mon 19 Oct | Review: impressions on 3+ days, first clicks, search terms, new negatives | Helen |

## 4. How we'll know it worked
- **First win:** impressions > 0, then on **3 or more days in a row**.
- **Then:** clicks, click-through rate, and the search-terms report filling with relevant terms.
- **Not yet judged:** enquiries/CPA — `form_submit` is still unconfirmed in GA4, so a real test enquiry through the quote form is also on your list.
- **Spend guard:** budget stays **£25/day**; no step here raises it. Any budget change goes through you.

## 5. Risks and honest limits
- I can't see Google's auction data without impressions, so steps 1–2 are how we get real information. This plan ranks levers by evidence; if the diagnosis surprises us, the table changes.
- Broader and more keywords raise the chance of irrelevant clicks. The 11 negatives are in place; I'll review the search-terms report weekly.
- The site fixes (7 copy fixes, legal placeholders, delivery wording) are still unapplied — worth doing before more paid traffic arrives.

---
_Rule G: `Charter-Rules.md`. Related: `Drafts/2026-10-07_Amfa_GoogleAds_CR-GA-0003_Wardrobes_v1.md`, `Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md` (Fitted Kitchens copy), `open-issues.md` `HI-8`._
