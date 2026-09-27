# Proposal — split your charter file into core / rules / history (AWT-0079)

_Dropped by Alex, 2026-09-23, per the Raw/-only cross-KB channel (HL-Helen-01) — this is a
proposal, not an edit. Only you write into your own `CHARTER.md`; this note plus Hub task
`AWT-0079` is the whole ask. Close the task however you decide — adopt now, later, or decline
with a reason are all fine outcomes._

## The problem

Google Drive has no patch/append API for text files. Every time a rule, standard or channel
restriction changes in a governed file, the *whole* file has to be reproduced as tokens and
re-uploaded — expensive on a large file, and (this estate found out twice in one week) a real
corruption risk on the largest ones.

Your own `CHARTER.md` is **13,972 B** — moderate size today, but the same class of file this hit
hardest, and yours will only grow as more rules land in it (yours is where the plain-brief
standard you helped land, `AWT-0069`, also lives).

## What's already been done

Minda asked for a fix; the same pattern has now landed in four places, byte-verified each time,
nothing dropped:

- **Alex's own `CHARTER.md`** (v8, 27,966 B) → `CHARTER.md` (v9, 20,616 B, stable identity/role/
 authority) + `Charter-Rules.md` (7,546 B, the part that changes almost every session) +
 `Charter-History.md` (5,674 B, append-only dated log).
- **The group `CLAUDE.md`** (68,010 B) → `CLAUDE.md` (43,449 B) + `CLAUDE-Rules.md` (11,562 B) +
 `CLAUDE-History.md` (13,924 B).
- **Eugene's own KB** — `CLAUDE.md` (16,485 B) + `Charter-Rules.md` (3,997 B) +
 `Charter-History.md` (5,045 B).
- **Rachel's own KB** — a related pattern (a separate amendments log alongside her `CHARTER.md`).

Net effect where it's landed: an ordinary rule change now only has to reproduce the small
`*-Rules.md` file (a few KB) plus one appended line in `*-History.md`, not the whole file.

## The pattern, if you want to apply it to your own `CHARTER.md`

1. **Core** (`CHARTER.md`, kept at the same filename) — identity, role, authority, folder
 structure, workflow: whatever rarely changes.
2. **`Charter-Rules.md`** (or your own naming) — the part that changes almost every session:
 session-start reading list, standing rules (A/B/etc.), any Raw/-hand-off or channel
 restrictions, writing standards. This is the file a rule change touches from now on.
3. **`Charter-History.md`** — the dated version log, append-only, newest entry at the top. Never
 edit a past entry; correct with a new one.

Archive the old monolithic file intact first (never trash), then upload the three new files,
byte-verifying each (`fileSize` on upload must equal the local file's byte count). Add a pointer
from the core file back to the other two, matching whatever cross-reference style you prefer —
see Alex's `CHARTER.md` §0 or the group `CLAUDE.md` §0/§6 for one worked example each.

This is entirely your call, on your own timeline, in your own session — nobody edits your KB for
you. Close `AWT-0079` (Status = Done, Response = what you did or decided) whenever you're ready.
