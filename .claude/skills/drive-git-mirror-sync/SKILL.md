---
name: drive-git-mirror-sync
description: Keep the Drive KB and the git mirror (minda-ui/Helen) byte-identical through the Composio CLI — compare by size per path, download or upload only what differs, then re-verify sizes. Use when Minda says "sync Drive files" or "mirror Drive into the repo". Drive is the source of truth.
---

# drive-git-mirror-sync

Why not the Drive MCP text export: it is lossy (escapes characters, changes line breaks) and `update_file` is metadata-only. The Composio CLI gives exact bytes and can overwrite in place.

## Compare (`plan.py` in this folder)
`python3 -I plan.py plan.json` lists each Drive folder (root, Drafts, Raw, Archive, change-log, `_unverified`, Brand-and-Voice, Research) via `GOOGLEDRIVE_FIND_FILE` and compares **name + size** with the repo: `new`, `changed`, `same-size`, `skip-pdf`. Edit the folder IDs if the KB moves. Run it with `-I` from a scratch directory.

## Drive → repo
For each `new`/`changed` file: `composio execute GOOGLEDRIVE_DOWNLOAD_FILE --account helen-googledrive -d '{ fileId: "<id>" }'` → it returns a signed `s3url` → `curl -fsSL -o <staging> "<url>"`. Check the byte size equals Drive's, copy into the repo, commit, push.

## Repo → Drive
- Existing file: `composio execute GOOGLEDRIVE_UPLOAD_UPDATE_FILE --account helen-googledrive --file <path> -d '{ fileId: "<id>" }'` (overwrites in place, same ID).
- New file: `GOOGLEDRIVE_UPLOAD_FILE --file <path> -d '{ folder_to_upload_to: "<folderId>" }'`.
- New folder: `GOOGLEDRIVE_CREATE_FOLDER -d '{ name: "…", parent_id: "<id>" }'`.
Run the commands from the repo root so `--file` resolves.

## Verify
Re-run `plan.py`: everything should be `same-size` except the known exceptions.

## Known exceptions (not errors)
- Two same-named 2026-09-28 change-logs in Drive: the repo keeps the larger (7,162 B) one.
- A Drive name containing `/` (HL-0014/HL-0018) is stored in the repo with `-`.
- 10 PDFs in Drive `Research/` are not mirrored.
- Drive `Raw/` originals may appear as `new` until archived.

## Rules
- Never delete in Drive (the settings deny `GOOGLEDRIVE_DELETE_*`). Before any trash/overwrite, re-check the file's `parentId` — a reused ID once trashed Alex's file (`HI-5`).
- If a write is blocked by the classifier, stop and tell Minda; do not route around it.
