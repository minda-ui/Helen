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

## Repo → Drive (estate standard: archive-then-recreate)
Use the estate skill `anthropic-skills:drive-sync-verified` (its `scripts/sync.sh`), one file at a time:
```
bash <path>/sync.sh <file> <drive-folder-id> --account helen-googledrive \
  --archive 176t4--VNBZB6IN4SOTAPQnV1nzS3OyHK --reason "<date> <what>" [--dry-run]
```
It archives the old copy to `Archive/` as "(archived …, superseded by …)", uploads the new one, and checks size, md5, byte-identical round-trip, no U+FFFD, exactly one live copy. **Dry-run first.** Folder ids: KB root `1H487UxvNabq1HK1NljhmEedvNA-l3XhX`, Drafts `1IRsNnTccB6y7FJD-Ko0362wq7DJqGWKN`, change-log `1CpQJ367LlzoiUuSVzwrK9rxje4WQzGLk`, Research `14EgBgGB5s0LcAym58jA8DngE8Sp8Eo2h`, Brand-and-Voice `1rElrjL68HQVy-DPlk_FhzkVDZgxxysqX`, Raw `1XhPXqOiNejXKBPCgOYPKusSGtnRkmUTH`, Skills `1v7r603-jF6FpElRWUDx-V-n952em8-mt`.
- **A replaced file gets a new Drive ID.** Never reuse an ID from earlier in a session or from notes — look the file up by folder and name.
- Do **not** overwrite in place (`GOOGLEDRIVE_UPLOAD_UPDATE_FILE`): it skips the archive step. (Done 2026-10-06 → 10-17 by mistake; versions survive in git and Drive revisions.)
- `--baseline origin/main` is omitted on purpose while the PR branch is ahead of `main`.
- New folder: `GOOGLEDRIVE_CREATE_FOLDER -d '{ name: "…", parent_id: "<id>" }'`.

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
