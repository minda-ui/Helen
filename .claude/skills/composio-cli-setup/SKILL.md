---
name: composio-cli-setup
description: Install and log in the Composio CLI in a fresh cloud session so Helen can reach Google Drive, Analytics and Ads when the MCP gateway is down or tools are missing. Use when `composio` is not found or `composio whoami` fails.
---

# composio-cli-setup

## Steps
1. **Check first:** `which composio` and `composio whoami`. If it works, stop.
2. **Download the installer to a scratch directory, read it** before running (it fetches a release from GitHub, verifies a checksum, and by default edits shell profiles and installs agent plugins): `curl -fsSL -o install.sh https://composio.dev/install`.
3. **Install without side effects:** `COMPOSIO_INSTALL_SHELL=none sh install.sh --no-plugins`. If it says it cannot find the latest release, pin a version: `… --no-plugins 0.4.1`. The entry point is `~/.local/bin/composio`.
4. **Log in as a human:** `composio login --no-browser` prints a URL. Give Minda the link, as a clickable link, and ask her to sign in with her own account.
5. **Wait in the background:** `composio login --poll` with `run_in_background` (it polls up to 10 minutes). You are notified when it finishes.
6. **Confirm:** `composio whoami` shows `minda@fishboneconstruction.co.uk`, org `minda_workspace`.

## Pitfalls
- **Never** `pkill -f "composio login"` — it matches the shell running the command and kills it. To restart, start a new `composio login --no-browser` and give the new URL.
- Never use `composio login --agent` when Minda is present; that is only for unattended runs.
- Never ask for or store a credential. Account aliases in use: `helen-googledrive`, `helen-googleads`, `helen-google-analytics`.
- `~/.local/bin` may not be on PATH — call `~/.local/bin/composio` explicitly.
- Writes may be blocked by the auto-mode classifier; see `drive-git-mirror-sync` and `google-ads-readonly-check` for what to do.
