# Change log — 2026-09-28 — Google Ads Composio link attempt, 5-day Google-side hold

_Append-only dated session file. Newest notes at the top. See `current-state.md` and `CHARTER.md`._

## Session — 2026-09-28

Handed over the Amfa Google Ads campaign plan (`Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md`) for Minda's first-campaign setup. She then asked to try connecting Google Ads via Composio directly (parallel route to `AWT-0132`, the provisioning request already sitting with Eugene).

No existing Google Ads connection anywhere in the org (`composio link googleads --list` → empty). Started a fresh link (`--alias helen-googleads --no-browser --no-wait`); Minda authorised via the printed URL. Checked status (`composio connections list --toolkit googleads`) — stuck at `INITIATED`, never reached `ACTIVE`. Minda reports Google's own flow told her a 5-day wait applies before proceeding further — a Google-side account/API review hold, not a Composio or Helen-side failure.

`open-issues.md` (`HI-8`) updated with this finding. Both routes to Ads access — Eugene's `AWT-0132` provisioning and this Composio link — may now be gated behind the same Google-side wait; nothing to configure from either until one clears.
