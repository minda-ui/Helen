# Change log — duplicate open-issues.md archived (Rung 2, Alex, ticked by Minda)

**Date:** 2026-09-18
**By:** Alex (AI Housekeeping & Operations Steward), Rung 2, dry-run presented and ticked by Minda
**Related:** Alex's `processed-items-ledger.md`, sister-KB Rung-2 sweep 2026-09-18

## What happened

A live scan of sister KBs for Rung-2 candidates found two `open-issues.md` files sitting side by
side in this KB's root, created ten minutes apart on 2026-09-16 — the older (`1FrlQYzJqmu3yIoiVimcC5ttMKVWoMQyn`,
4,257 B, ends at HI-4) had never been archived when the newer version (`1uxNReHtDkDn4sytbRZZ3hhSWyUuZ9GO3`,
5,380 B, adds HI-5) was created, breaking Helen's own archive-then-recreate convention just this once.

Verified content before touching anything: the newer file is byte-identical to the older through HI-4,
plus the added HI-5 row — a clean superset, nothing to reconcile or lose.

## Fix applied

Moved the older file into `Archive/` (metadata-only, bytes untouched, still 4,257 B), renamed to match
this KB's own naming convention: `open-issues.md (archived 2026-09-16 1845, superseded by the version
adding HI-5)`.

## Not touched

The live `open-issues.md` (`1uxNReHtDkDn4sytbRZZ3hhSWyUuZ9GO3`) and its content are unchanged. No other
files in this KB were read or modified during this sweep.
