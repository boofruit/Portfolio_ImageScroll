"""Write sets/manifest.json listing every project folder and its files.

Runs in GitHub Actions before the site is deployed, so the page can load
one static file instead of calling the GitHub API on every visit.
"""

import json
from pathlib import Path

ROOT = Path("sets")


def sort_key(name: str):
    return name.casefold()


folders = []
for folder in sorted((p for p in ROOT.iterdir() if p.is_dir()), key=lambda p: sort_key(p.name)):
    files = sorted((f.name for f in folder.iterdir() if f.is_file()), key=sort_key)
    folders.append({"name": folder.name, "path": f"{ROOT.name}/{folder.name}", "files": files})

out = ROOT / "manifest.json"
out.write_text(json.dumps({"folders": folders}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {out} with {len(folders)} folders")
