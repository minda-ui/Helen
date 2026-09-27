# Change log — 2026-09-19 — External-binary-document relay-to-Alex rule added

_Append-only dated session file. Newest notes at the top. See `current-state.md` and `CHARTER.md`._

## Session — 2026-09-19: standing external-binary-document-relay clause added to CHARTER.md §2a

Minda approved an estate-wide rule (`HL-0014` / `HL-0018` on the group Help & Lessons desk,
`7780569054316420`) and asked for it to be propagated identically into each AI employee's own charter,
Helen's included, for consistency. This session applied that single, pre-decided change to Helen's
`CHARTER.md` — no new policy was made here.

**Change:** added one bullet to `CHARTER.md` §2a ("May, without asking"), directly after the existing
"Help & Lessons" bullet — the same section that already carries this kind of standing operational
protocol:

> **External binary documents.** If your routine or session fetches an external binary document (e.g. a
> PDF from an API or web source) too large to safely relay through model context as base64, do not
> attempt the relay yourself. Register it using its permanent source URL and a checksum, leave a short
> covering note, and flag it to Alex — the estate's standing fetch-and-relay owner (HL-0014 / HL-0018).

**Mechanics (this KB's standing archive-then-recreate convention, Drive has no in-place content edit):**
- Archived the live `CHARTER.md` (`1l8rCk5csHcjxZKP4BMRWZX9GikiZdPqL`, 10,782 B) into `Archive/`, renamed
  `CHARTER.md (archived 2026-09-19, superseded by adding the estate-wide external-binary-document-relay-
  to-Alex rule, HL-0014/HL-0018)`.
- Created a new `CHARTER.md` (`1-efk20plUGLmqjTmg3gyD8Uji1v6hrju`) in the KB root with the identical
  original content plus the one inserted bullet above — nothing else reworded or restructured.
- Verified byte-for-byte: local reconstructed file was 11,194 B; the first upload attempt landed at
  11,193 B (a dropped trailing newline from how the content was typed into the create call, not a
  content truncation) — caught by the size check, the file was trashed and recreated with the trailing
  newline restored, landing at 11,194 B exactly matching the local reconstruction.

**Freshness note.** The file ID this task named as "the live charter" (`1VG_aLPm9pnXIwkyecrkav8cSl3Mw24b8`)
turned out on a fresh `get_file_metadata` check to already be an archived copy (titled `CHARTER.md
(archived 2026-09-14 2000, superseded by Help & Lessons update)`, sitting in `Archive/`), not the live
file — a stale ID from whenever this task was written. The actual live file was found by searching this
KB's root for `title = 'CHARTER.md'`, which returned `1l8rCk5csHcjxZKP4BMRWZX9GikiZdPqL` (the one
carrying the 2026-09-14 Help & Lessons addition). Worked from that instead, per this KB's own
"work from what you actually read, not cached knowledge" practice.

**Open / next.** None. This was a self-contained, owner-approved mechanical edit; no other charter
section, control file, or draft was touched.
