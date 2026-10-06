# Change log — 2026-10-04 — Google Ads reconnected and diagnosed; second routine added; CHARTER.md restored after being misfiled

_Append-only dated session file. Newest notes at the top. See `current-state.md` and `CHARTER.md`._

## Session — 2026-10-04

**Composio Google Ads connection genuinely active.** The 2026-09-28 attempt had expired rather than activating. A fresh `composio link googleads` authorised cleanly and reached `ACTIVE` immediately — no multi-day hold this time. Verified it actually works (Rule C, not just the status flag): `GOOGLEADS_LIST_ACCESSIBLE_CUSTOMERS` returned the real Amfa account, then `GOOGLEADS_GET_CAMPAIGN_BY_NAME` confirmed the live "Amfa - Bespoke Kitchens - Search" campaign.

**Zero-impression diagnosis and fix.** Pulled a performance snapshot at Minda's request — 0 impressions/clicks/spend over the campaign's first 5 days (30 Sept–4 Oct). Diagnosed properly rather than guessing: account, billing, campaign serving status, budget status, and ad approval/review status were all ruled out as genuinely healthy via direct GAQL queries. Root cause: 3 of the original 4 keywords carried `systemServingStatus: RARELY_SERVED`, leaving the campaign running on effectively one keyword. Drafted and added 6 broader keyword variants (phrase match, grounded in already-confirmed Amfa facts) directly to the live ad group via `GOOGLEADS_MUTATE_AD_GROUP_CRITERIA`. Verified all 10 keywords live afterward. `Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md` §3 updated to match.

**Second routine added.** Minda asked directly for a recurring Ads performance check. Added "Helen — Amfa Google Ads Performance Check" (`trig_01GM29cwxU5S2ctxAkUYC885`, every 2 days, 08:47 Europe/London) to `CHARTER.md` §6, deleted the now-redundant one-off reminder that had been scheduled earlier.

**CHARTER.md found misfiled and restored.** While syncing the §6 update, discovered `CHARTER.md` was no longer in the KB root — moved into `Archive/` on 2026-09-30 and mislabeled as superseded by the charter split, a rationale that doesn't hold (the split happened 2026-09-23 and made all three files permanent siblings). No live `CHARTER.md` existed in the KB root for several days; nothing in this session actually broke from it since local git/context had the correct cached content. Restored to the root with its correct title, carrying the §6 update in the same restore. Misfiled `Archive/` copy left untouched as a forensic record, per the `HI-5` precedent. Logged as `HI-11` (resolved same session).

**Stray duplicate files found, not acted on.** While locating the canonical campaign-plan file, a Drive-wide search surfaced two extra native-Google-Docs copies under an unidentified parent folder. Not touched (`HI-5` lesson); logged as `HI-10`, open, low confidence.

All three control files (`CHARTER.md`, `open-issues.md`, `Charter-History.md`) synced to Drive (create-new → verify-old → trash-old) and committed/pushed to git.
