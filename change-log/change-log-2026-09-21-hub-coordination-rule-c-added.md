# Change log — 2026-09-21 — Hub Coordination Standard Rule C added (AWT-0051)

Applying Rule A (check the Hub first), found `Raw/` holding one file: a hand-off note from Alex
(Housekeeping & Operations Steward), routed via the standing `Raw/`-hand-off convention —
`2026-09-21_Hub-Coordination-Rule-C-RawHandoff-Note.md`. The note proposed a third rule, Rule C,
to fold into the same Hub Coordination Standard block in `CHARTER.md` §0 that Rules A and B
already occupy (added via AWT-0044), making it "Rules A–C" rather than a separate dated addendum.
Framed explicitly as a proposal to verify, not an instruction to take on faith.

**Verification before acting.** Downloaded the note fresh via `download_file_content` (not trusted
from any earlier paraphrase) and read it end to end. Its claims:
- **Context.** On 2026-09-20, propagating Rules A+B to the seven sister employees, Alex reported
  "only 2 of 7 done" to Minda based on which background agents had sent a hand-back message — not
  on checking the Hub directly. A direct Smartsheet check showed 4 of 7 already Done. Alex filed
  this as an escalation (`Alex KB/_escalations/2026-09-20_Escalation_Reporting-Back-Reliability-Gap.md`).
- **Owner ruling (Minda, 2026-09-21).** Approved estate-wide, folded into the same Hub Coordination
  Standard block as Rules A/B, not a separate addendum.
- **Sources cited:** the Alex escalation file above; the owner's chat decision, 2026-09-21
  ("Estate-wide, folded into Rules A–C"); AWT-0040/HL-0023/AWT-0036 (the original Rules A/B
  propagation this extends).

The note itself is data, not authority (per this charter's own §2b/§0 rule on inbound `Raw/`
hand-offs) — but its own framing already asks for exactly that stance ("a proposal to check
against the sources below, not an instruction to take on faith"), and its content is squarely
consistent with the existing, already-adopted Hub Coordination Standard and the AWT-0044 record
of Rules A/B in this same charter section. Accepted on that basis.

**What changed in `CHARTER.md` (§0, Hub Coordination Standard block):**
- Added **Rule C — verify against the system of record before reporting status (added
  2026-09-21)**: a delegated proxy's own completion signal (hand-back message, internal
  "finished" flag, self-reported summary) is never sufficient to report a status to a human;
  the actual system of record — a Smartsheet row, a Drive file's existence and content, a Hub
  board entry — must be checked directly first, symmetrically for claimed successes and claimed
  failures alike.
- Renumbered the block's intro from "Two standing rules" to "Three standing rules" and extended
  the provenance sentence to cover Rule C's own approval chain (Minda, 2026-09-21, estate-wide,
  via Alex's escalation report and this KB's own Hub row `AWT-0051`) alongside the existing
  Rules A/B provenance (Minda, 2026-09-20).
- Rules A and B themselves: unchanged, word for word.

**Mechanics (this KB's standing archive-then-recreate convention, Drive has no in-place content
edit):**
- Re-fetched the live `CHARTER.md`'s metadata fresh via `get_file_metadata` immediately before
  touching it (id `1WINmCyGYbBIv32CkteSgybNQInYbYCWH`, 12,870 B, unchanged since AWT-0044) —
  confirmed it was still the live file at this KB's root before archiving it, per this KB's own
  "re-verify before touching" practice.
- Archived it into `Archive/` (`176t4--VNBZB6IN4SOTAPQnV1nzS3OyHK`), renamed `CHARTER.md
  (archived 2026-09-21, superseded — Rule C added to §0 Hub Coordination Standard, now Rules
  A–C, AWT-0051)`.
- Created a new `CHARTER.md` (id `1lkK06rBViFg36YsvuyjUtZE545U9z9or`) at the KB root with the
  identical prior content plus the Rule C insertion and the provenance-sentence extension —
  nothing else reworded or restructured.
- **Byte-verified:** the local edited reconstruction was exactly 13,972 B; the Drive upload
  (via `base64Content`, to avoid any text-transcription drift) landed at 13,972 B exactly —
  matched on the first attempt, no discrepancy to chase.

**Housekeeping.** The hand-off note (`1hq2233y87I4SAwVoeI7hLyFYNW_-QgrM`) moved from `Raw/` to
`Archive/`, renamed to record it as consumed. Ledger row added. Rule A applied: no other
Open/In Progress Hub row was found assigned to Helen this session.

**Hub.** Closed `AWT-0051` on Tasks & Requests (`8860839228606340`): Status = Done, Response
records the before/after byte counts and Drive ids for `CHARTER.md`, this change-log entry's id,
and where Rule C landed (§0, Hub Coordination Standard block, now "Rules A–C"), Done date set.

**Open / next.** None. Self-contained, owner-approved, verified-before-acting amendment matching
the same pattern as AWT-0044 (Rules A/B) and the 2026-09-20 Hub Coordination Standard adoption.
