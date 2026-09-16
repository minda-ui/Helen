# Change log — 2026-09-16 — Alex's open-issues.md trashed in error (HI-5)

_Append-only dated session file. Newest notes at the top. See `current-state.md` and `CHARTER.md`._

## Session — 2026-09-16: charter §2b boundary breach during routine Drive cleanup

**What happened.** After recording Minda's approval of the two Construction drafts, Helen recreated
several of her own stale Drive control files (`current-state.md`, `processed-items-ledger.md`, the two
drafts, the review file, a new change-log entry) as part of the normal "create new, trash the stale
duplicate" pattern used throughout this KB's Drive syncing (Drive has no in-place content-update tool).

When trashing the stale duplicate of Helen's own `open-issues.md`, Helen reused a file ID
(`1VPYo3Skzi8IyiUoTT0oRtczJKV1sZ7d0`) that had been read earlier in the same session — but that ID
actually belonged to **Alex's** `open-issues.md` (Alex's KB, Drive folder
`1QGc0EqThFDAIP7QYvGY1DEhliSbMTGNe`), fetched while checking with Alex's charter about where to report
`AWT-0006`/`AWT-0007` completion, several turns earlier. Helen called `trash_file` on it, believing it
was her own stale copy (id `1OGTnYf0SVpGukNBVwGFu3IQnOHDLchhI`).

This is a direct breach of `CHARTER.md` §2b: *"Edit, move or delete anything in a sister KB... she does
not write to them — there is no §7a hand-off role for Helen."*

**Caught immediately.** The very next Drive action (trashing what should have been Helen's own
`current-state.md`/`processed-items-ledger.md` duplicates) went fine, but on reaching `open-issues.md`
Helen paused to double-check IDs given the stakes of an open-issues control file, called
`get_file_metadata` on `1VPYo3Skzi8IyiUoTT0oRtczJKV1sZ7d0`, and got "Requested entity was not found."
`download_file_content` on the same id also failed. Helen has **no untrash/restore tool** in this
session's toolset (`trash_file` only moves to trash; there is no corresponding restore call), so this
could not be self-corrected.

**Assessment:** the file is very likely still recoverable. Google Drive moves trashed files to a Trash
folder rather than deleting them outright; they're typically retained for a window (commonly ~30 days)
before permanent deletion, and can be restored by anyone with edit access via the Drive web UI (or an
API call this session doesn't have). Nothing suggests permanent deletion has happened.

**Actions taken:**
1. Correctly identified and trashed Helen's own actual stale `open-issues.md` (`1OGTnYf0SVpGukNBVwGFu3IQnOHDLchhI`,
   verified via `get_file_metadata` — confirmed `parentId` was Helen's own KB folder — before trashing).
2. Logged `HI-5` in this file (`open-issues.md`), Critical, explaining what happened and what's needed.
3. Added a **Critical** row to the group Help & Lessons desk (`7780569054316420`, row `245986763605892`)
   so Alex — who won't necessarily read Helen's KB — sees this independently and can verify its own KB's
   integrity once the file is restored.
4. Updated `current-state.md` to surface this prominently at the top of "Last session" and "Next action,"
   not buried.

**Open / next.** `HI-5` stays open until someone with Drive restore access (human, or an Alex/Eugene
session with the right tool) recovers the file from Trash. Once restored, Alex should verify its content
is intact (nothing else in that session's Drive actions should have touched it, but worth confirming)
before closing `HI-5`. Process lesson for Helen going forward: **never reuse a Drive file ID across a
sister-KB lookup and a same-named-file trash/recreate action** — always re-verify `parentId` via
`get_file_metadata` immediately before any `trash_file` call, not just for control files but for anything
where an ID could plausibly have been read from another KB earlier in the same session.
