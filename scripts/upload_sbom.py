import json
import sys
import os
import datetime
import subprocess
from logger import log, group_start, group_end, notice

def main():
    if len(sys.argv) < 4:
        log.error("Missing arguments: <file_path> <target> <repo>")
        sys.exit(1)

    file_path = sys.argv[1]
    target = sys.argv[2]
    repo = sys.argv[3]

    group_start(f"Dependency Graph Upload: {target}")

    sha = os.environ.get("GITHUB_SHA")
    ref = os.environ.get("GITHUB_REF")
    run_id = os.environ.get("GITHUB_RUN_ID", "manual")

    if not os.path.exists(file_path):
        log.error(f"SBOM file not found: {file_path}")
        group_end()
        sys.exit(1)

    try:
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

        log.info(f"Submitting snapshot for {target} (Correlator: wolfi-fips-{target})")
        
        result = subprocess.run(
            ["gh", "api", f"/repos/{repo}/dependency-graph/snapshots", "--method", "POST", "--input", "-"],
            input=json.dumps(payload),
            text=True,
            capture_output=True
        )

        if result.returncode != 0:
            log.error(f"GitHub API Error: {result.stderr}")
            sys.exit(1)

        notice(f"Successfully uploaded SBOM for {target}. Results will overwrite previous {target} entries.")
        
    except Exception as e:
        log.error(f"Unexpected error during upload: {str(e)}")
        sys.exit(1)
    finally:
        group_end()

if __name__ == "__main__":
    main()