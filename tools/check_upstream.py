"""Read-only upstream release check. Requires GitHub CLI; never changes files."""
from pathlib import Path
import json
import subprocess

manifest = json.loads((Path(__file__).resolve().parents[1] / "apps.json").read_text())
for app in manifest["apps"]:
    repo = app["upstream"]["repository"].split("github.com/", 1)[1]
    result = subprocess.run(["gh", "api", "repos/" + repo + "/releases/latest", "--jq", ".tag_name"], capture_output=True, text=True)
    if result.returncode:
        print(app["id"] + ": could not verify latest release")
        continue
    latest = result.stdout.strip()
    recorded = app["upstream"]["releaseTag"]
    print(app["id"] + ": recorded=" + recorded + " latest=" + latest + (" — current" if latest == recorded else " — review update"))
