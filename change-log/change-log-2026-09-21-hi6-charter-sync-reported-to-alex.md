# Change log — 2026-09-21 — HI-6 raised, reported to Alex

Minda: "Report it to Alex via Fishbone Workforce" — following the failed attempt to clear the
`CHARTER.md` git-sync block even with a scoped Bash permission rule added.

**Logged HI-6** in `open-issues.md` — full sequence: Rule C landed in Drive's `CHARTER.md` via Alex's
background-agent dispatch (`AWT-0051`) before this session started; independently verified; git sync
blocked twice (Instruction Poisoning, then Self-Modification on a revert attempt); a scoped Bash
permission rule added at Minda's request didn't clear it either (same "Self-Modification" reason on
retry); an unrelated `.gitignore` commit in the same session went through cleanly, confirming the block
is specific to `CHARTER.md` content, not a general restriction.

**Raised `HL-Helen-01`** on the shared Help & Lessons desk (`7780569054316420`), Category "Governance
question", Priority High, Status Open, Owner/helper = Alex, Applies to = estate-wide (the Raw/-hand-off
+ background-agent-dispatch pattern, not just Helen's own KB). The point flagged for Alex specifically:
the equivalent charter edit went through cleanly this morning via the background-agent-impersonation
route Alex dispatched, with no visible block — while the identical class of change is being stopped
when attempted transparently, in Helen's own live session, with a full audit trail and explicit human
confirmation. That's backwards from a safety standpoint, and worth Alex's and Minda's judgement on
whether the propagation pattern itself needs a look, independent of resolving this one file.

**Status:** Genuinely unresolved. Drive's `CHARTER.md` is correct and current (source of truth); the
git mirror is one commit behind on that file only. No further in-session attempt planned — reporting it
was the ask, not forcing a fix through.
