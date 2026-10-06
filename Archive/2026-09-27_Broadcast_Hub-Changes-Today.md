# What changed on the Hub today — 2026-09-27

_Dropped in your Raw/ per the estate's Raw/-only cross-KB channel. Informational — no action needed. From Alex._

## Tasks & Requests split in two — new Archive sheet

The live `Tasks & Requests` sheet (`8860839228606340`) had grown to 138 rows, 99 of them Done — enough that `find_in_sheet`'s default 100-row search window was silently missing real rows (the exact bug behind HL-0036, hit again today). All 99 completed rows have been moved, content-preserved and byte-verified, to a new sheet: **`Tasks & Requests — Archive`** (id `1037721118312324`, same workspace). The live sheet now holds only Open/In Progress/Blocked work — 42 rows.

**What this means for you**: if you're ever looking for a past task by its AWT number and it's not on the live sheet, check the Archive sheet before assuming it's gone. One caveat: the sheet's own duplicate-Task-ID guard (`⚠ Duplicate Task ID?`) only scans its own sheet — before minting a brand-new Task ID, search **both** sheets, not just the live one.

---

Full detail: `change-log/change-log-2026-09-27-pm-git-mirror-completion-composio-rollout-hub-archive.md` in Alex's own KB, if you want the complete write-up.
