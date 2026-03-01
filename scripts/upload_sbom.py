import json
import sys
import os
import datetime
import subprocess
from typing import Dict, Any
from logger import log, group_start, group_end, notice

class DependencyUploader:
    def __init__(self, file_path: str, target: str, repo: str):
        self.file_path = file_path
        self.target = target
        self.repo = repo
        self.sha = os.environ.get("GITHUB_SHA")
        self.ref = os.environ.get("GITHUB_REF")
        self.run_id = os.environ.get("GITHUB_RUN_ID", "manual")
        self.scanned_time = datetime.datetime.now().isoformat()

    def _get_ecosystem(self, purl: str) -> str:
        if not purl or not purl.startswith("pkg:"):
            return "other"
        try:
            return purl.split(":")[1].split("/")[0].lower()
        except (IndexError, AttributeError):
            return "other"

    def _build_payload(self) -> Dict[str, Any]:
        if not os.path.exists(self.file_path):
            log.error(f"File not found: {self.file_path}")
            sys.exit(1)

        with open(self.file_path, "r") as f:
            sbom_data = json.load(f)

        components = sbom_data.get("components", [])
        log.info(f"Processing {len(components)} components from {self.file_path}")

        ecosystems: Dict[str, Dict[str, Any]] = {}

        for comp in components:
            purl = comp.get("purl")
            if not purl:
                continue

            eco = self._get_ecosystem(purl)
            if eco not in ecosystems:
                ecosystems[eco] = {}

            ecosystems[eco][purl] = {
                "package_url": purl,
                "relationship": "direct",
                "scope": "runtime",
                "metadata": {
                    "ecosystem": eco
                }
            }

        manifests = {}
        for eco, deps in ecosystems.items():
            manifest_id = f"{self.target}/{eco}"
            manifests[manifest_id] = {
                "name": manifest_id,
                "file": {"source_location": self.file_path},
                "resolved": deps
            }

        return {
            "version": 0,
            "sha": self.sha,
            "ref": self.ref,
            "job": {
                "correlator": f"wolfi-fips-{self.target}",
                "id": self.run_id
            },
            "detector": {
                "name": "wolfi-fips-uploader",
                "version": "1.2.0",
                "url": "https://github.com/taha2samy"
            },
            "scanned": self.scanned_time,
            "manifests": manifests
        }

    def run(self):
        group_start(f"Upload SBOM: {self.target}")
        try:
            payload = self._build_payload()
            
            log.info(f"Uploading to {self.repo} via GitHub API")
            log.info(f"Detected ecosystems: {list(payload['manifests'].keys())}")

            result = subprocess.run(
                ["gh", "api", f"/repos/{self.repo}/dependency-graph/snapshots", 
                 "--method", "POST", "--input", "-"],
                input=json.dumps(payload),
                text=True,
                capture_output=True
            )

            if result.returncode != 0:
                log.error(f"API Error: {result.stderr.strip()}")
                sys.exit(1)

            notice(f"Successfully updated dependency graph for {self.target}")
            
        except Exception as e:
            log.error(f"Execution failed: {str(e)}")
            sys.exit(1)
        finally:
            group_end()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        log.error("Usage: python3 upload_sbom.py <FILE_PATH> <TARGET> <REPO>")
        sys.exit(1)

    uploader = DependencyUploader(
        file_path=sys.argv[1],
        target=sys.argv[2],
        repo=sys.argv[3]
    )
    uploader.run()