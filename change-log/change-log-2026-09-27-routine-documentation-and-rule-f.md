# Change log — 2026-09-27 — AWT-0134 (routine documentation gap) and AWT-0146 (Rule F) folded in

_Append-only dated session file. Newest notes at the top. See `current-state.md` and `CHARTER.md`._

## Session — 2026-09-27: two Raw/ hand-offs from Alex actioned

Minda asked to go ahead with both. Read all three notes waiting in `Raw/` first (the routine-gap proposal, the Rule F hand-off, and the informational Hub-changes-today broadcast that `AWT-0146` bundled in with it).

**AWT-0134 — routine documentation gap.** The note claimed a "Helen — Task Check-in" routine (`trig_01AJ2vd3rxuishiThgSJ38sT`, weekdays 10:00 UTC) has been live since 2026-09-15, while `CHARTER.md` §6 and `current-state.md` both still said "no scheduled routine yet." Per Rule C, didn't take the note's word for it: a direct `get_trigger` lookup on the trigger ID came back not-found (expected — routines are scoped to the session that created them, not visible cross-session), so instead checked the Hub Roster (`8154403007760260`) directly. It independently confirms the same routine, same trigger ID, same cadence, documented there since 2026-09-16 (over a week before today's note) — and Eugene's row shows the identical pattern rolled out the same day. Treated as verified. Rewrote `CHARTER.md` §6 to document the routine properly (trigger id, cadence, what it reads from the Hub, what it writes, its draft-only boundary) and corrected `current-state.md`'s Mode field.

**AWT-0146 — Rule F.** Owner-approved estate-wide (Minda, quoted in the hand-off note): any shared-space change (a Hub sheet, a shared Drive structure, anything more than one employee reads) must be both registered (a Hub row) and broadcast (a `Raw/` note to everyone affected) — being within your own authority to make the change doesn't excuse skipping either half. Added as **Rule F** in `Charter-Rules.md`, next to Rules A–C/E. The companion broadcast note (Tasks & Requests split into a live sheet + new `Tasks & Requests — Archive` sheet, id `1037721118312324`, since `find_in_sheet`'s default 100-row window was silently missing rows past 100) needed no charter action — informational only — but its caveat (search *both* sheets before minting a new Task ID) was worth acting on: retroactively checked `AWT-0158` (registered earlier this session) against the Archive sheet too. No collision.

**Both files rewritten archive-then-recreate + byte-verified** (`CHARTER.md`, `Charter-Rules.md`), consistent with how every prior charter change in this KB has been done. `Charter-History.md` got two new dated entries. All 3 Raw/ notes moved to `Archive/`. Both Hub rows (`AWT-0134`, `AWT-0146`) closed Done with a Response describing what changed and where.

## Control files

`processed-items-ledger.md` (rows 25–26) and `current-state.md` rewritten in the same pass (create-new + verify + trash-old, re-verifying `parentId` before each `trash_file` call per the `HI-5` lesson).

## Git mirror

Synced `CHARTER.md`, `Charter-Rules.md`, `Charter-History.md`, `current-state.md`, `processed-items-ledger.md` to `minda-ui/Helen` in the same pass as the Composio-rollout files from earlier this session.
