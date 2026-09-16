# Change log — 2026-09-15 — www subdomain block noted in Construction Brand-and-Voice

_Append-only dated session file. Newest notes at the top. See `current-state.md` and `CHARTER.md`._

## Session — 2026-09-15: hostname note added to `Fishbone-Construction-Ltd.md`

Minda asked whether `www.fishboneconstruction.co.uk` was reachable. It isn't — `WebFetch` returned
`EGRESS_BLOCKED` and a raw `curl` CONNECT tunnel to it returned 403. The bare domain
(`fishboneconstruction.co.uk`, no `www.`) works fine on both — confirmed HTTP 200 via `curl` and a
successful `WebFetch` fetch, content matching what's already on file (HSRC-08).

`Brand-and-Voice/Fishbone-Construction-Ltd.md` already only used the bare domain, so no facts were
wrong, but nothing recorded *why* — added a short hostname note under the header so a future session
doesn't retry `www.` and mistake it for the site being down. Updated in both the git mirror and the
Drive copy (Drive file recreated with the new content; the stale version trashed, not left in the
folder alongside it).
