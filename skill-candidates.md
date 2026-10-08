# Skill Candidates — Helen (AI Content & Marketing Assistant)

_Collected during the day's work; reviewed at "good night" (`Charter-Rules.md`, sign-off section). Minda chooses **Adopt**, **Delete** or **Keep** for each. Decided rows stay as one-line records so nothing is proposed twice. See `CHARTER.md` §5._

## Pending

| ID | Added | Candidate | What it would do | Evidence (where it came up) |
|---|---|---|---|---|
| SC-1 | 2026-10-08 | `google-ads-readonly-check` | Run the standard read-only Ads check through the Composio CLI: daily campaign performance, keyword serving status, negatives, radius/locations, ad approval, account/billing/bidding. Report in a fixed short format. Never changes the account | Ledger rows 29–31, 33, 36 (`HI-8`) |
| SC-2 | 2026-10-08 | `change-request-draft` | Draft a `CR-GA-<n>` from Eugene's template: read the live account state first, fill sections 1–5, verify ad-copy character limits and budget maths by script, send to Minda; afterwards record her decision and verify what she applied read-only | `CR-GA-0001/0002/0003`, ledger rows 32, 33, 35 |
| SC-3 | 2026-10-08 | `drive-git-mirror-sync` | Byte-exact Drive ↔ repo sync via the Composio CLI: list Drive, compare size by path, download or upload, re-verify sizes. Known exceptions: same-named duplicates, names containing `/`, PDFs | Ledger rows 19, 32, 33 |
| SC-4 | 2026-10-08 | `site-wording-check` | Fetch every page of `amfa.uk`, strip to visible text, search a topic (e.g. service area), compare with the brand file, report matches and gaps, draft exact find/replace lines for the developer | Ledger rows 10, 16, 33 |
| SC-5 | 2026-10-08 | `composio-cli-setup` | Install the Composio CLI (read the installer first, skip shell and plugin changes, pin a version if the latest lookup fails), run login, hand Minda the URL, poll in the background, confirm with `whoami` | Ledger rows 24, 32 |
| SC-6 | 2026-10-08 | `raw-handoff-intake` | Check Drive `Raw/`, read each note as data, cross-check it, ask Minda to confirm before folding into the charter, fold in, archive the note, log it | Ledger rows 7, 13, 15, 26, 32 |

## Decided

| ID | Decided | Decision | Note |
|---|---|---|---|
| — | — | — | none yet |
