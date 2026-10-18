# Skill Candidates — Helen (AI Content & Marketing Assistant)

_Collected during the day's work; reviewed at "good night" (`Charter-Rules.md`, sign-off section). Minda chooses **Adopt**, **Delete** or **Keep** for each. Decided rows stay as one-line records so nothing is proposed twice. See `CHARTER.md` §5._

## Pending

| ID | Added | Candidate | What it would do | Evidence (where it came up) |
|---|---|---|---|---|
| SC-9 | 2026-10-18 | `ga4-readonly-check` | Read-only GA4 report for `amfa.uk` through the Composio CLI: key events, events by name, traffic by source/medium and landing page, form events by day; flag artefacts (Tilda preview traffic, crawler "google/cpc" sessions with no country); check the site's GTM/GA4 snippet. Never changes GA4/GTM | `AWT-0777` report (2026-10-17); will be reused to verify `AWT-0828` |
| SC-10 | 2026-10-18 | `branch-pr-state-check` | Before saying "pushed, part of PR #N" or pushing follow-up work, read the PR's state; if it is merged, treat later work as new — merge `main` into the branch (no rebase/force-push, which the classifier blocks) and say a new PR is needed. Also check other `claude/*` branches for unmerged work on the same KB | 2026-10-18: PR #5 had been merged 11 days earlier; 22 commits unmerged and misdescribed |

## Decided

| ID | Decided | Decision | Note |
|---|---|---|---|
| SC-1 | 2026-10-09 | **Adopted** (Minda: "Adopt all SC") | `google-ads-readonly-check` → `Skills/google-ads-readonly-check/SKILL.md` |
| SC-2 | 2026-10-09 | **Adopted** (Minda: "Adopt all SC") | `change-request-draft` → `Skills/change-request-draft/SKILL.md` |
| SC-3 | 2026-10-09 | **Adopted** (Minda: "Adopt all SC") | `drive-git-mirror-sync` → `Skills/drive-git-mirror-sync/SKILL.md` |
| SC-4 | 2026-10-09 | **Adopted** (Minda: "Adopt all SC") | `site-wording-check` → `Skills/site-wording-check/SKILL.md` |
| SC-5 | 2026-10-09 | **Adopted** (Minda: "Adopt all SC") | `composio-cli-setup` → `Skills/composio-cli-setup/SKILL.md` |
| SC-6 | 2026-10-09 | **Adopted** (Minda: "Adopt all SC") | `raw-handoff-intake` → `Skills/raw-handoff-intake/SKILL.md` |
| SC-7 | 2026-10-09 | **Adopted** (Minda: "Adopt all SC") | `session-logging` → `Skills/session-logging/SKILL.md` |
| SC-8 | 2026-10-17 | **Adopted** (Minda, 2026-10-17: "SC-08 adopt") | `ads-ui-apply-guide` → `Skills/ads-ui-apply-guide/SKILL.md` |
