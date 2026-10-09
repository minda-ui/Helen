import json, os, subprocess, sys

CLI = os.path.expanduser("~/.local/bin/composio")
REPO = "/home/user/Helen"
ACCT = "helen-googledrive"
FOLDERS = {
    "": "1H487UxvNabq1HK1NljhmEedvNA-l3XhX",
    "Drafts": "1IRsNnTccB6y7FJD-Ko0362wq7DJqGWKN",
    "Raw": "1XhPXqOiNejXKBPCgOYPKusSGtnRkmUTH",
    "Archive": "176t4--VNBZB6IN4SOTAPQnV1nzS3OyHK",
    "change-log": "1CpQJ367LlzoiUuSVzwrK9rxje4WQzGLk",
    "_unverified": "1SLhyi1ql5IixJtcOOcrCOWkGJTZ7N4HE",
    "Brand-and-Voice": "1rElrjL68HQVy-DPlk_FhzkVDZgxxysqX",
    "Research": "14EgBgGB5s0LcAym58jA8DngE8Sp8Eo2h",
}
FOLDER_MIME = "application/vnd.google-apps.folder"


def run(slug, data):
    p = subprocess.run([CLI, "execute", slug, "--account", ACCT, "-d", json.dumps(data)],
                       capture_output=True, text=True, timeout=120)
    out = p.stdout
    return json.loads(out[out.index("{"):])


def list_folder(fid):
    files, tok = [], None
    while True:
        d = {"q": f"'{fid}' in parents and trashed = false", "pageSize": 100,
             "fields": "nextPageToken,files(id,name,mimeType,size,modifiedTime)"}
        if tok:
            d["pageToken"] = tok
        r = run("GOOGLEDRIVE_FIND_FILE", d)
        data = r["data"]
        files += data.get("files") or data.get("response_data", {}).get("files", [])
        tok = data.get("nextPageToken") or data.get("response_data", {}).get("nextPageToken")
        if not tok:
            return files


plan = []
for rel, fid in FOLDERS.items():
    for f in list_folder(fid):
        if f["mimeType"] == FOLDER_MIME:
            continue
        if f["mimeType"] == "application/pdf" or f["name"].lower().endswith(".pdf"):
            plan.append({**f, "path": os.path.join(rel, f["name"]), "action": "skip-pdf"})
            continue
        path = os.path.join(rel, f["name"])
        local = os.path.join(REPO, path)
        size = int(f.get("size") or 0)
        if not os.path.exists(local):
            act = "new"
        elif os.path.getsize(local) != size:
            act = "changed"
        else:
            act = "same-size"
        plan.append({**f, "path": path, "action": act})

json.dump(plan, open(sys.argv[1], "w"), indent=1)
for a in ("new", "changed", "same-size", "skip-pdf"):
    items = [p for p in plan if p["action"] == a]
    print(f"== {a}: {len(items)}")
    if a in ("new", "changed"):
        for p in items:
            print("  ", p["path"], p.get("size"))
