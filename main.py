
import os
import json
import hcl2
from datetime import datetime


def load_json(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def load_hcl(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = hcl2.load(f)
        return {
            key: value.get("default")
            for variable in data.get("variable", [])
            for key, value in variable.items()
        }
    except Exception:
        return {}


def define_env(env):
    base_dir = os.path.dirname(os.path.abspath(__file__))

    bake_vars = load_hcl(os.path.join(base_dir, "docker-bake.hcl"))
    version_vars = load_hcl(os.path.join(base_dir, "versions.hcl"))
    summary = load_json(os.path.join(base_dir, "reports", "summary.json"))
    benchmarks = load_json(os.path.join(base_dir, "reports", "benchmark_data.json"))

    meta_root = os.path.join(base_dir, "all-metadata")
    distroless_meta = load_json(os.path.join(meta_root, "distroless_attestation_details.json"))
    standard_meta = load_json(os.path.join(meta_root, "standard_attestation_details.json"))
    dev_meta = load_json(os.path.join(meta_root, "development_attestation_details.json"))

    stats = summary.get("summary", {}).get(
        "statistic",
        {"passed": 0, "failed": 0, "broken": 0, "total": 0},
    )

    owner = bake_vars.get("OWNER", "taha2samy")
    repo = bake_vars.get("REPO_NAME", "wolfi-openssl-fips")

    env.variables.update(
        {
            "project_name": os.getenv("PROJECT_NAME", "Wolfi OpenSSL FIPS"),
            "owner": owner,
            "repo_name": repo,
            "registry": bake_vars.get("REGISTRY", "ghcr.io"),
            "core_version": bake_vars.get("CORE_VERSION", "3.5.5"),
            "fips_version": bake_vars.get("FIPS_VERSION", "3.1.2"),
            "base_image": version_vars.get("BASE_IMAGE", "N/A"),
            "static_image": version_vars.get("STATIC_IMAGE", "N/A"),
            "generation_date": os.getenv(
                "GENERATION_DATE", datetime.utcnow().strftime("%Y-%m-%d")
            ),
            "test_stats": stats,
            "test_badge_color": "red"
            if (stats["failed"] + stats["broken"]) > 0
            else "brightgreen",
            "benchmark_data": benchmarks,
        }
    )

    env.variables["packages"] = [
        {
            "name": key.replace("_VER", "").replace("_", " ").title(),
            "version": value,
        }
        for key, value in version_vars.items()
        if key not in {"BASE_IMAGE", "STATIC_IMAGE"}
    ]

    env.variables.update(
        {
            "distroless_digest": distroless_meta.get("provenance", {}).get("digest", "N/A"),
            "distroless_url": distroless_meta.get("provenance", {}).get("url", "#"),
            "distroless_sbom_url": distroless_meta.get("sbom", {}).get("url", "#"),
            "standard_digest": standard_meta.get("provenance", {}).get("digest", "N/A"),
            "standard_url": standard_meta.get("provenance", {}).get("url", "#"),
            "standard_sbom_url": standard_meta.get("sbom", {}).get("url", "#"),
            "dev_digest": dev_meta.get("provenance", {}).get("digest", "N/A"),
            "dev_url": dev_meta.get("provenance", {}).get("url", "#"),
            "dev_sbom_url": dev_meta.get("sbom", {}).get("url", "#"),
        }
    )

    env.variables["github"] = {
        "repository": os.getenv("GITHUB_REPOSITORY", f"{owner}/{repo}"),
        "commit_sha": os.getenv("GITHUB_SHA", "0000000"),
        "run_id": os.getenv("GITHUB_RUN_ID", "#"),
    }

    @env.macro
    def render_test_status(status: str) -> str:
        icons = {"passed": "✅", "failed": "❌", "broken": "💥"}
        return icons.get(status, "❓")

