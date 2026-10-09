---
name: session-logging
description: Close out each unit of Helen's work the same way — HI-/ledger/change-log entries, commit and push to the PR branch, upload changed files to Drive, re-verify sizes. Use after any check, draft or change, and at "good night".
---

# session-logging

## After a task (when Minda says "log it to HI-8", or a draft/check is done)
1. **Count figures by script** before writing them down (statuses, characters, totals). Don't count by eye.
2. **`open-issues.md`:** append a dated sentence to the relevant `HI-<n>` row (never delete; resolved issues get a `Resolved` line). Past entries are never edited — correct with a new entry that names the error.
3. **`processed-items-ledger.md`:** add the next row (company, channel, status, draft location). One row per brief/draft/check.
4. **`change-log/change-log-YYYY-MM-DD-<slug>.md`:** one file per day; append a bullet per item, including anything that went wrong.
5. **Commit + push** to the session branch (never `main` directly); end commits with the attribution lines. Retry a failed push once — it can be transient.
6. **Upload to Drive** (`drive-git-mirror-sync`): `UPLOAD_UPDATE_FILE` for existing files, `UPLOAD_FILE` for new ones. Drive is the source of truth; the repo mirrors it.
7. **Re-verify sizes**; report in one short line (Rule E).

## At "good night" (`Charter-Rules.md` sign-off)
1. Today's change-log exists and covers everything. 2. Ledger row for anything drafted/logged. 3. `HI-<n>` rows touched are current. 4. Refresh `current-state.md`. 5. Show the Pending skill candidates; Minda chooses Adopt / Delete / Keep. 6. One short line, then sign off.
