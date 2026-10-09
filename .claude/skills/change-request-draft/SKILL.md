---
name: change-request-draft
description: Draft a Google Ads Change Request (CR-GA-<n>) for Minda to approve and apply, from Eugene's template — read live account state first, fill sections 1–5, verify ad-copy limits and budget maths by script, then record her decision and verify what she applied. Use for any proposed live change to the Ads account.
---

# change-request-draft

**Why (Rule G):** a live-account change is a real-world financial transaction. Helen prepares; **Minda applies**. Never execute the change.

## Steps
1. **State the goal and the metric first.** No change without a success measure and a review date.
2. **Read the live state** (use `google-ads-readonly-check`): the CR must say what exists now (locations, keywords, budget, bidding), not assume it.
3. **Copy the template** `Research/2026-10-06_GoogleAds_Change-Request-Template_from-Eugene.md` to `Drafts/YYYY-MM-DD_Amfa_GoogleAds_CR-GA-<nnnn>_<slug>_v1.md`. Next number = highest existing `CR-GA-` + 1.
4. **Fill sections 1–5:** goal/metric/review dates · exact changes (table: type, item, match type, value, rationale) · budget impact (current → proposed, expected change, worst case) · how to undo · risk flags. Leave **section 6 (approval) and 7 (post-apply check) blank.**
5. **Verify by script before sending:**
   - RSA headlines ≤ 30 and descriptions ≤ 90 characters; WhatsApp starter ≤ 140; the stated lengths in brackets are correct.
   - Budget maths: monthly maximum = daily budget × 30.4 (Google may spend up to 2× on a single day, never more than 30.4× per month).
6. **Facts:** every claim traces to a source (live page, brand file). No superlatives, no invented figures. Broad match only with negatives, a cap and a first-week search-terms review — say so.
7. **Hand over:** send the file to Minda (`SendUserFile`) with the how-to-apply steps in the Ads UI.
8. **After she applies:** read-only verify what actually changed, then fill section 6 ("Applied (where/when)") truthfully — including anything she did differently (CR-GA-0001: she added two different broad keywords). Update the status line. Section 7 at the review date.
9. Log with `session-logging`.
