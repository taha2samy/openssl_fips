import json
import sys
import os
import datetime
import subprocess

def main():
    if len(sys.argv) < 4:
        sys.exit(1)

    file_path = sys.argv[1]
    target = sys.argv[2]
    repo = sys.argv[3]

    sha = os.environ.get("GITHUB_SHA")
    ref = os.environ.get("GITHUB_REF")
    run_id = os.environ.get("GITHUB_RUN_ID", "manual")

    with open(file_path, "r") as f:
        data = json.load(f)

    resolved = {}
    for comp in data.get("components", []):
        purl = comp.get("purl")
        if purl:
            resolved[purl] = {
                "package_url": purl,
                "relationship": "direct",
                "scope": "runtime"
            }

    payload = {
        "version": 0,
        "sha": sha,
        "ref": ref,
        "job": {
            "correlator": f"wolfi-fips-{target}",
            "id": run_id
        },
        "detector": {
            "name": "wolfi-sbom-uploader",
            "version": "1.0.0",
            "url": "https://github.com/taha2samy"
        },
        "scanned": datetime.datetime.now().isoformat(),
        "manifests": {
            f"manifest-{target}": {
                "name": f"wolfi-{target}",
                "file": {"source_location": file_path},
                "resolved": resolved
            }
        }
    }

    subprocess.run(
        ["gh", "api", f"/repos/{repo}/dependency-graph/snapshots", "--method", "POST", "--input", "-"],
        input=json.dumps(payload),
        text=True,
        check=True
    )

if __name__ == "__main__":
    main()