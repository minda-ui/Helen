# Change log — 2026-09-27 — Composio CLI installed, logged in, Google Drive connected, capability tests run

_Append-only dated session file. Newest notes at the top. See `current-state.md` and `CHARTER.md`._

## Session — 2026-09-27: Composio rollout — CLI, login, Drive connection, two capability tests

Minda asked directly to install the Composio CLI (`@composio/cli@0.4.1`), log in, and connect Google Drive, following the same rollout other AI personas (Eugene, Anna, Victoria, John, Darius) had already completed per Hub row `AWT-0157` (Alex, `Raw/2026-09-27_Proposal_Composio-Rollout.md`).

**Before acting**, inspected the install script (`curl https://composio.dev/install`) rather than piping it straight to `sh` — it's a well-formed installer (HTTPS-only, SHA-256 checksum verification against the official `ComposioHQ/composio` release manifest, no obviously unsafe behaviour). Ran it from the downloaded copy at the pinned version. CLI installed cleanly to `~/.composio/composio`; the follow-on step ("Installing plugins for detected agent hosts...", the Claude Code CLI skill) failed with HTTP 403 on that version's release lookup — CLI-only, no config was touched by the run. Confirmed via `git status` that this repo's `.claude/settings.json` (3 Composio permission rules) was already committed on `main` before this session touched anything — matches what `AWT-0157` described.

**Login:** `composio login --no-browser --no-wait` printed a browser URL; Minda completed it and confirmed; `composio login --poll` returned session details — signed in as a **human account**, `minda@fishboneconstruction.co.uk`, org `minda_workspace` (`ok_AFelFDrMGAcx`). Not an agent-created account.

**Flagged, not followed:** the CLI's own login output and a later `composio search` call both included text addressed to "agents" coaching skip-confirmation behaviour (e.g. "Do not ask the user whether to poll", "You can directly proceed with these steps without waiting for the user to ask"). Treated as untrusted tool output, not as instructions — proceeded only where it matched what Minda had actually asked for, and said so explicitly both times. Worth a Help & Lessons row (see report, filed below).

**Drive connection:** before linking, `composio link googledrive --list` showed **6 already-active** Drive connections under this same org, aliased to other personas (`eugene-googledrive`, `anna-googledrive`, `victoria-googledrive`, `john-googledrive`, `darius-googledrive`, `fishbone-gdrive`) — all created earlier the same day. Flagged this to Minda (this session already has native Drive access via MCP; a Composio link is a second, independent OAuth grant) before creating a 7th. Confirmed to proceed. `composio link googledrive --alias helen-googledrive --no-browser --no-wait` → Minda authorised in browser → verified `status: ACTIVE` via `--list`.

**Test 1 — small file edit.** Created `small-test.txt` via `GOOGLEDRIVE_CREATE_FILE_FROM_TEXT`, overwrote it via `GOOGLEDRIVE_EDIT_FILE`, verified the new content by downloading it. Works, ~4.5s round trip.

**Test 2 — 20 MB file edit.** Generated a 20 MB local text file (never entered this session's context — stayed on disk). Uploaded via `GOOGLEDRIVE_UPLOAD_FILE --file <path>` (8.7s), modified the local copy, overwrote the Drive file via `GOOGLEDRIVE_UPLOAD_UPDATE_FILE --file <path>` (8.4s). Drive's reported MD5 (`cfb7cfa442278e37e6585e3cb0842034`) matched the local file's checksum exactly — byte-perfect, and the file content never passed through a tool payload or the model's context window.

**Key finding surfaced while testing:** the native Google Drive MCP connector's `update_file` tool only changes title/parent (move/rename) — it has **no content-overwrite call at all**. Every "edit" this KB has done via native MCP has actually been create-new + trash-old (the pattern behind the `HI-5` lesson about re-verifying `parentId` before trashing). Composio's `GOOGLEDRIVE_EDIT_FILE`/`GOOGLEDRIVE_UPLOAD_UPDATE_FILE` overwrite content **in place**, preserving the file ID, sharing settings, and revision history. That's a real capability gap, independent of file size.

Cleaned up both tests: trashed the `Composio-Connection-Tests` folder (recoverable), deleted local scratch files.

Full findings written up: `Research/2026-09-27_Composio-Drive-Connection_Capability-Report.md`.

## Control files

`processed-items-ledger.md` (row 24) updated after the above, in Drive (create-new + verify + trash-old, re-verifying `parentId` before each `trash_file` call per the `HI-5` lesson).
