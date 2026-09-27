# Change log — 2026-09-15 — Construction website research blocked (HI-4)

_Append-only dated session file. Newest notes at the top. See `current-state.md` and `CHARTER.md`._

## Session — 2026-09-15: HI-4 opened — network egress blocked

Minda asked Helen to check `www.fishboneconstruction.co.uk`. `WebFetch` returned
`EGRESS_BLOCKED` — this session's network policy restricts outbound access and can't reach the
domain. Retried after Minda asked whether an update had landed; same result, so the policy hadn't
changed (or a new session hadn't been started against an updated one).

Searched the group **AI Workforce Hub** and found the task this maps to: **`AWT-0011`**
(`Tasks & Requests` sheet, row `32778681452420`) — requested by Minda, relayed by Alex: research
`fishboneconstruction.co.uk` (home, services, about/history, projects/case-studies) read-only via
WebFetch, cite facts never invent, and build `Brand-and-Voice/Fishbone-Construction.md` on the same
pattern as Amfa. Explicitly unblocks `AWT-0006` (Construction case study) and the remaining part of
`AWT-0007` (Construction/Properties social posts). Priority High, due 2026-09-22.

**Actions taken:**
- Updated `AWT-0011` on the Hub: Status → **Blocked**, Response explains the `EGRESS_BLOCKED` reason
  and the two ways to unblock (widen the environment's network policy + fresh session, or Minda
  supplies the site content as a PDF/screenshots into `Research/`, the pattern already used for
  Amfa's future-website copy). Health auto-flipped to Red on the Blocked status.
- User asked directly whether this had been reported — realised the Hub update alone wasn't enough;
  **logged it in Helen's own KB too**: `HI-4` in `open-issues.md`, and `current-state.md` updated.
  Two separate records (Hub task status, and Helen's own issue log) should both reflect a blocker
  like this, not just one.

**Open / next.** HI-4 stays open until one of the two unblock paths happens. Construction's
Brand-and-Voice work (HI-3) is stalled on this specifically — Amfa remains the only company with a
real voice reference right now.
