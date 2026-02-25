import os
import json
import hcl2
import sys
import csv
from datetime import datetime

# Path setup for internal modules
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)

from scripts.logger import log, group_start, group_end

def load_json(path: str) -> dict:
    if not os.path.exists(path):
        log.warning(f"File not found: {path}")
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        log.error(f"Failed to parse JSON at {path}: {str(e)}")
        return {}

def load_hcl(path: str) -> dict:
    if not os.path.exists(path):
        log.warning(f"File not found: {path}")
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = hcl2.load(f)
        return {
            key: value.get("default")
            for variable in data.get("variable", [])
            for key, value in variable.items()
        }
    except Exception as e:
        log.error(f"Failed to parse HCL at {path}: {str(e)}")
        return {}

def define_env(env):
    group_start("MkDocs Data Injection")
    
    # 1. Embedded CSV Data for Vega-Lite
    csv_path = os.path.join(ROOT_DIR, "docs/assets/data/results.csv")
    csv_values = []
    if os.path.exists(csv_path):
        try:
            with open(csv_path, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                csv_values = list(reader)
        except Exception as e:
            log.error(f"Failed to read CSV: {str(e)}")
    
    # 2. Configuration & Statistics
    bake_vars = load_hcl(os.path.join(ROOT_DIR, "docker-bake.hcl"))
    version_vars = load_hcl(os.path.join(ROOT_DIR, "versions.hcl"))
    summary = load_json(os.path.join(ROOT_DIR, "reports", "summary.json"))
    raw_benchmarks = load_json(os.path.join(ROOT_DIR, "reports", "benchmark_data.json"))

    # 3. Supply Chain Metadata
    meta_root = os.path.join(ROOT_DIR, "all-metadata")
    distroless_meta = load_json(os.path.join(meta_root, "distroless_attestation_details.json"))
    standard_meta = load_json(os.path.join(meta_root, "standard_attestation_details.json"))
    dev_meta = load_json(os.path.join(meta_root, "development_attestation_details.json"))

    # 4. Processing Test Stats
    stats = summary.get("summary", {}).get(
        "statistic",
        {"passed": 0, "failed": 0, "broken": 0, "total": 0}
    )

    # 5. Benchmark Fallback (prevents template errors if JSON is missing)
    if not raw_benchmarks or "metrics" not in raw_benchmarks:
        log.warning("Benchmark JSON missing. Injecting empty fallback structure.")
        benchmarks = {
            "metadata": {"fips": {"openssl_version": "N/A"}},
            "metrics": {
                "AES-256-GCM": {"fips": [0]*6, "ubuntu": [0]*6, "debian": [0]*6, "alpine": [0]*6},
                "sha256": {"fips": [0]*6, "ubuntu": [0]*6, "debian": [0]*6, "alpine": [0]*6},
                "sha512": {"fips": [0]*6, "ubuntu": [0]*6, "debian": [0]*6, "alpine": [0]*6},
                "sha3-256": {"fips": [0]*6, "ubuntu": [0]*6, "debian": [0]*6, "alpine": [0]*6}
            }
        }
    else:
        benchmarks = raw_benchmarks

    owner = bake_vars.get("OWNER", "taha2samy")
    repo = bake_vars.get("REPO_NAME", "wolfi-openssl-fips")

    # 6. Global Variable Injection
    env.variables.update({
        "project_name": os.getenv("PROJECT_NAME", "Wolfi OpenSSL FIPS"),
        "owner": owner,
        "repo_name": repo,
        "registry": bake_vars.get("REGISTRY", "ghcr.io"),
        "core_version": bake_vars.get("CORE_VERSION", "3.5.5"),
        "fips_version": bake_vars.get("FIPS_VERSION", "3.1.2"),
        "base_image": version_vars.get("BASE_IMAGE", "N/A"),
        "static_image": version_vars.get("STATIC_IMAGE", "N/A"),
        "generation_date": os.getenv("GENERATION_DATE", datetime.utcnow().strftime("%Y-%m-%d")),
        "test_stats": stats,
        "test_badge_color": "red" if (stats["failed"] + stats["broken"]) > 0 else "brightgreen",
        "benchmark_data": benchmarks,
        "bench_results_raw": json.dumps(csv_values) # Embedded for Vega-Lite
    })

    # 7. Dependency List
    env.variables["packages"] = [
        {"name": key.replace("_VER", "").replace("_", " ").title(), "version": value}
        for key, value in version_vars.items()
        if key not in {"BASE_IMAGE", "STATIC_IMAGE"}
    ]

    # 8. Provenance & SBOM URLs
    env.variables.update({
        "distroless_digest": distroless_meta.get("provenance", {}).get("digest", "N/A"),
        "distroless_url": distroless_meta.get("provenance", {}).get("url", "#"),
        "distroless_sbom_url": distroless_meta.get("sbom", {}).get("url", "#"),
        "standard_digest": standard_meta.get("provenance", {}).get("digest", "N/A"),
        "standard_url": standard_meta.get("provenance", {}).get("url", "#"),
        "standard_sbom_url": standard_meta.get("sbom", {}).get("url", "#"),
        "dev_digest": dev_meta.get("provenance", {}).get("digest", "N/A"),
        "dev_url": dev_meta.get("provenance", {}).get("url", "#"),
        "dev_sbom_url": dev_meta.get("sbom", {}).get("url", "#"),
    })

    env.variables["github"] = {
        "repository": os.getenv("GITHUB_REPOSITORY", f"{owner}/{repo}"),
        "commit_sha": os.getenv("GITHUB_SHA", "0000000"),
        "run_id": os.getenv("GITHUB_RUN_ID", "#"),
    }

    @env.macro
    def render_test_status(status: str) -> str:
        icons = {"passed": "✅", "failed": "❌", "broken": "💥"}
        return icons.get(status, "❓")

    log.info("Documentation context successfully injected.")
    group_end()