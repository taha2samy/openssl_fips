import os
import sys
import json
import hcl2
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

with open("all-metadata/distroless_attestation_details.json", "r") as f:
    distroless_outputs = json.load(f)

with open("all-metadata/standard_attestation_details.json", "r") as f:
    standard_outputs = json.load(f)

with open("reports/benchmark_summary.md", "r") as f:
    summary_performance_results = f.read()

def env(name: str, default: str | None = None) -> str:
    value = os.getenv(name, default)
    if value is None:
        return ""
    return value

def load_hcl_variables(file_path):
    if not os.path.exists(file_path):
        return {}
    
    with open(file_path, 'r') as f:
        data = hcl2.load(f)
    
    flat_vars = {
        k: v.get('default') 
        for var in data.get('variable', []) 
        for k, v in var.items()
    }
    return flat_vars

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(base_dir)
    template_dir = os.path.join(project_root, "templates")
    output_file = os.path.join(project_root, "README.md")

    bake_path = os.path.join(project_root, "docker-bake.hcl")
    bake_vars = load_hcl_variables(bake_path)

    versions_path = os.path.join(project_root, "versions.hcl")
    versions_vars = load_hcl_variables(versions_path)

    base_image = versions_vars.get("BASE_IMAGE", "N/A")
    static_image = versions_vars.get("STATIC_IMAGE", "N/A")
    
    packages = {
        k: v for k, v in versions_vars.items() 
        if k not in ["BASE_IMAGE", "STATIC_IMAGE"]
    }

    summary_path = os.path.join(project_root, "reports/summary.json")
    test_stats = {'passed': 0, 'failed': 0, 'broken': 0, 'total': 0}
    if os.path.exists(summary_path):
        with open(summary_path, 'r') as f:
            summary_json = json.load(f)
            test_stats = summary_json.get('summary', {}).get('statistic', test_stats)

    comparison_path = os.path.join(project_root, "Comparison_Report.md")
    table_of_comparison = ""
    if os.path.exists(comparison_path):
        with open(comparison_path, 'r') as f:
            table_of_comparison = f.read()

    owner = bake_vars.get("OWNER", "taha2samy")
    repo_name = bake_vars.get("REPO_NAME", "wolfi-openssl-fips")
    registry = bake_vars.get("REGISTRY", "ghcr.io")
    core_version = bake_vars.get("CORE_VERSION", "3.5.5")
    fips_version = bake_vars.get("FIPS_VERSION", "3.1.2")
    
    repo_url = env("REPO_URL", f"https://github.com/{owner}/{env('CODE_REPO_NAME', 'openssl_fips')}")

    context = {
        "project_name": env("PROJECT_NAME", "Wolfi OpenSSL FIPS"),
        "owner": owner,
        "repo_name": repo_name,
        "repo_url": repo_url,
        "code_repo_name": env("CODE_REPO_NAME", "openssl_fips"),
        "registry": registry,
        "summary_performance_results": summary_performance_results,
        
        "core_version": core_version,
        "fips_version": fips_version,
        
        "distroless_size": env("DISTROLESS_SIZE", "N/A"),
        "standard_size": env("STANDARD_SIZE", "N/A"),
        
        "table_of_comparison": table_of_comparison,
        "base_image": base_image,
        "static_image": static_image,
        "packages": packages,
        "test_stats": test_stats,
        "distroless_url": distroless_outputs["provenance"]["url"],
        "standard_url": standard_outputs["provenance"]["url"],
        "distroless_digest": distroless_outputs["provenance"]["digest"],
        "standard_digest": standard_outputs["provenance"]["digest"],
        "distroless_sbom_url": distroless_outputs["sbom"]["url"],
        "standard_sbom_url": standard_outputs["sbom"]["url"],
        
        "generation_date": env("GENERATION_DATE", datetime.utcnow().strftime("%Y-%m-%d")),
        "build_date": env("BUILD_DATE", datetime.utcnow().strftime("%Y%m%d")),
    }

    if not os.path.exists(template_dir):
        print(f"Error: Template directory not found at {template_dir}")
        sys.exit(1)

    try:
        env_jinja = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=False,
            keep_trailing_newline=True,
        )

        template = env_jinja.get_template("README.md.j2")
        rendered_content = template.render(context)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(rendered_content)

        print(f"README.md successfully generated at: {output_file}")

    except Exception as e:
        print(f"Error generating README: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()