import os
import json
import hcl2
import sys
from datetime import datetime

# Setup path to import from scripts
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)

from scripts.logger import log, group_start, group_end, notice

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
    group_start("MkDocs Environment Injection")
    
    # 1. Load All Data Sources
    bake_vars = load_hcl(os.path.join(ROOT_DIR, "docker-bake.hcl"))
    version_vars = load_hcl(os.path.join(ROOT_DIR, "versions.hcl"))
    summary = load_json(os.path.join(ROOT_DIR, "reports", "summary.json"))
    raw_benchmarks = load_json(os.path.join(ROOT_DIR, "reports", "benchmark_data.json"))

    meta_root = os.path.join(ROOT_DIR, "all-metadata")
    distroless_meta = load_json(os.path.join(meta_root, "distroless_attestation_details.json"))
    standard_meta = load_json(os.path.join(meta_root, "standard_attestation_details.json"))
    dev_meta = load_json(os.path.join(meta_root, "development_attestation_details.json"))

    # 2. Process Test Statistics
    stats = summary.get("summary", {}).get(
        "statistic",
        {"passed": 0, "failed": 0, "broken": 0, "total": 0}
    )

    # 3. Benchmark Fallback Logic
    if not raw_benchmarks or "metrics" not in raw_benchmarks:
        log.warning("benchmark_data.json is missing or invalid. Using safety fallback.")
        benchmarks = {
            "metadata": {"fips": {"openssl_version": "N/A"}, "ubuntu": {}, "alpine": {}, "debian": {}},
            "metrics": {
                "AES-256-GCM": {"fips": [0]*6, "ubuntu": [0]*6, "debian": [0]*6, "alpine": [0]*6},
                "sha256": {"fips": [0]*6, "ubuntu": [0]*6, "debian": [0]*6, "alpine": [0]*6},
                "sha512": {"fips": [0]*6, "ubuntu": [0]*6, "debian": [0]*6, "alpine": [0]*6},
                "sha3-256": {"fips": [0]*6, "ubuntu": [0]*6, "debian": [0]*6, "alpine": [0]*6}
            }
        }
    else:
        benchmarks = raw_benchmarks

    # 4. Global Variables Injection
    owner = bake_vars.get("OWNER", "taha2samy")
    repo = bake_vars.get("REPO_NAME", "wolfi-openssl-fips")

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
    })

    # 5. Packages List
    env.variables["packages"] = [
        {"name": key.replace("_VER", "").replace("_", " ").title(), "version": value}
        for key, value in version_vars.items()
        if key not in {"BASE_IMAGE", "STATIC_IMAGE"}
    ]

    # 6. Attestation Metadata
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

    log.info("Environment variables successfully injected into MkDocs.")
    group_end()