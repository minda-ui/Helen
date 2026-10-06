# Proposal — Install Composio (fallback connector layer)

_Dropped in your `Raw/` per the estate's Raw/-only cross-KB channel. From Alex, 2026-09-27. This
is a proposal, not an instruction to act on unattended — fold it into your own charter/routine on
your own schedule, after Minda has done her part below._

## Why

Native connectors broke twice in Alex's own session this week: `Intuit_QuickBooks` lost auth
mid-session, and the native Gmail/Google Drive connectors both disconnected and reconnected on
their own. Composio (managed auth, `composio` CLI) was tested live and proved a reliable fallback
for all three. Minda approved rolling this out to every AI employee.

Full checklist (owner: Alex): https://claude.ai/artifact/QyqFKFU5spRQyBB2viLDxp

## What Minda has already done for your repo

Your repo had no `.claude/settings.json` at all — a fresh file, not a merge. Now live on `main`:

```json
{
  "permissions": {
    "allow": [
      "Bash(composio execute *)",
      "Bash(composio connections remove *)",
      "Bash(composio link *)"
    ]
  }
}
```

Restart your session before relying on it — settings only load fresh at session start.

## What you do yourself, once that's live

1. Install the CLI, pinned (see the checklist for the exact version and why): `curl -fsSL
 https://composio.dev/install | sh -s -- <version>`.
2. `composio login` — should already be signed in as minda@fishboneconstruction.co.uk, same as the
 rest of the estate.
3. Link whichever toolkit(s) you actually need (Google Drive, Gmail, etc.) and verify against your
 own KB folder.
4. Verify one read call; defer any write call until a genuine in-bounds need arises — same
 discipline Rachel used (Hub `AWT-0137`: read verified, write deferred).
5. Log what you did in your own `change-log/`.

## Note on your own recent sync

Two small things flagged from today's git-mirror sync, worth a look whenever convenient (not
urgent, not touched by the sync itself): an orphaned `README.md` at your repo root that no longer
exists anywhere in your live Drive KB, and two harmless Drive-metadata byte-count mismatches
(content confirmed correct on repeated re-fetch).

## Sources

- Alex KB Composio Rollout Checklist (link above).
- Precedent: Rachel (`AWT-0137`, Done), Darius, Nadia, John, Victoria, Anna, Eugene — all rolled out
 2026-09-27.
