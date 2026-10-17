# Change log — 2026-10-17 — CR-GA-0004 (Fitted Kitchens ad group)

**Session by:** Claude, on behalf of minda@fishboneconstruction.co.uk

- Read-only Ads checks (skill `google-ads-readonly-check`) on 2026-10-10, 10-14, 10-17: no change; still 0 impressions since 30 Sept; no setting blocking.
- Drafted `Drafts/2026-10-17_Amfa_GoogleAds_CR-GA-0004_Fitted-Kitchens_v1.md` (skill `change-request-draft`): Fitted Kitchens ad group, 7 phrase keywords, 1 RSA, 3 negatives, `/kitchens`; all 19 ad lines and the budget maths verified by script (3 stated lengths were wrong on first pass and were corrected before sending). Section 6 awaits Minda.
- Plan copy changed: removed "Fitted in 3–8 Weeks" (site FAQ: production + installation 6–10 weeks), "Budget-Friendly, Built to Last", "Quality Kitchens, Fair Prices".
- **Process note:** since 2026-10-06 Drive replacements were done by in-place overwrite (`UPLOAD_UPDATE_FILE`), not the estate's archive-then-recreate standard (skill `drive-sync-verified`). No data lost — every version is in git history and Drive revisions — but the old copies were not moved to `Archive/`. From today Drive writes use the estate script; `Skills/drive-git-mirror-sync` to be updated. Raised with Minda.
- Logged to `open-issues.md` HI-8, ledger row 41. Nothing applied to the account.
- **Later:** Minda said "Approve as-is" for CR-GA-0004. Recorded in section 6; not yet applied. Her answer on "from £2,000" for fitted kitchens was not given separately — approval taken as accepting the copy as written.
- **Applied:** Minda built CR-GA-0004 in the Ads UI with step-by-step screenshot guidance. Caught and corrected along the way: she opened "New campaign" (wrong screen) twice — redirected to Ad groups; the ad's final URL defaulted to the homepage and the headlines/descriptions to Google AI prefills — both fixed before saving; 3 AI sitelinks removed.
- **Verification found:** the first save created the ad group and ad with **0 keywords**; Minda added the 7 afterwards (4 `ELIGIBLE`, 3 `RARELY_SERVED`). Negatives `cheap`, `flat pack`, `flatpack` were added at ad-group level, broad match, instead of campaign-level phrase — recorded in CR section 6, left as is (narrower effect, no harm).
- Logged to HI-8, ledger row 42. Next: read-only check ~2026-10-19; reviews 10-24 and 10-31.
- **Good-night check:** refreshed `current-state.md`; added SC-8 `ads-ui-apply-guide` to `skill-candidates.md`; showed the candidate list to Minda.
