import json
import os
import re
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from urllib.parse import quote

ALLURE_RESULTS_DIR = "allure-results"
REPORTS_DIR = "reports"
DOCS_DIR = "docs"
TEMPLATES_DIR = "templates"
SUMMARY_OUTPUT_PATH = os.path.join(REPORTS_DIR, "summary.json")
DETAILED_DOC_PATH = os.path.join(DOCS_DIR, "TEST_RESULTS.md")
VERSIONS_HCL_PATH = "versions.hcl"
DOCKER_BAKE_HCL_PATH = "docker-bake.hcl"

def parse_hcl_variable(file_path, var_name):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            match = re.search(r'variable\s+"' + var_name + r'"\s+{\s*default\s*=\s*"([^"]+)"', content)
            if match:
                return match.group(1)
            
            # Fallback for base images format (sometimes slightly different)
            match_digest = re.search(r'variable\s+"' + var_name + r'"\s+{\s*default\s*=\s*"([^"]+@[^"]+)"', content)
            if match_digest:
                return match_digest.group(1)
    except FileNotFoundError:
        return "N/A"
    return "N/A"

def extract_build_info():
    fips_ver = parse_hcl_variable(DOCKER_BAKE_HCL_PATH, "FIPS_VERSION")
    core_ver = parse_hcl_variable(DOCKER_BAKE_HCL_PATH, "CORE_VERSION")
    registry = parse_hcl_variable(DOCKER_BAKE_HCL_PATH, "REGISTRY")
    owner = parse_hcl_variable(DOCKER_BAKE_HCL_PATH, "OWNER")
    repo = parse_hcl_variable(DOCKER_BAKE_HCL_PATH, "REPO_NAME")
    
    base_img = parse_hcl_variable(VERSIONS_HCL_PATH, "BASE_IMAGE")
    static_img = parse_hcl_variable(VERSIONS_HCL_PATH, "STATIC_IMAGE")

    return {
        "fips_version": fips_ver,
        "core_version": core_ver,
        "registry": registry,
        "owner": owner,
        "repo_name": repo,
        "base_image": base_img,
        "static_image": static_img
    }

def extract_package_versions():
    packages = []
    try:
        with open(VERSIONS_HCL_PATH, 'r') as f:
            content = f.read()
            matches = re.findall(r'variable\s+"([A-Z_]+_VER)"\s+{\s*default\s*=\s*"([^"]+)"', content)
            for name, ver in matches:
                clean_name = name.replace("_VER", "").replace("_", " ").title()
                packages.append({"name": clean_name, "version": ver})
    except FileNotFoundError:
        pass
    return packages

def parse_allure_results():
    suites = {}
    total_stats = {'passed': 0, 'failed': 0, 'broken': 0, 'total': 0}
    
    for root, _, files in os.walk(ALLURE_RESULTS_DIR):
        for file in files:
            if file.endswith("-result.json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path) as f:
                        data = json.load(f)
                        
                        status = data.get('status', 'unknown')
                        total_stats['total'] += 1
                        if status in total_stats:
                            total_stats[status] += 1
                        
                        description = next((p['value'] for p in data.get('parameters', []) if p['name'] == 'description'), 
                                           data.get('description', ''))
                        
                        test_detail = {
                            'name': data.get('name', 'Unknown Test'),
                            'status': status,
                            'status_icon': {'passed': '✅', 'failed': '❌', 'broken': '💥'}.get(status, '❓'),
                            'duration_ms': data.get('stop', 0) - data.get('start', 0),
                            'fullName': data.get('fullName', ''),
                            'description': description.replace('\n', '  \n') if description else '',
                            'error_trace': data.get('statusDetails', {}).get('trace', '')
                        }
                        
                        # Group by Suite (File Name)
                        suite_raw = data.get('fullName', 'Unknown').split('::')[0]
                        suite_name = os.path.basename(suite_raw)
                        
                        if suite_name not in suites:
                            suites[suite_name] = []
                        suites[suite_name].append(test_detail)
                        
                except Exception:
                    continue
    
    # Sort suites and tests for consistency
    sorted_suites = {k: sorted(v, key=lambda x: x['name']) for k, v in sorted(suites.items())}
    return sorted_suites, total_stats

def main():
    suites, stats = parse_allure_results()
    build_info = extract_build_info()
    package_versions = extract_package_versions()
    badge_color = "red" if stats['failed'] + stats['broken'] > 0 else "brightgreen"

    badge_text = (
        f"failed {stats['failed'] + stats['broken']}"
        if badge_color == "red"
        else f"passed {stats['passed']}"
    )

    badge_url = f"https://img.shields.io/badge/tests-{quote(badge_text)}-{badge_color}"

    # Generate Badge URL
    summary_data = {
        'statistic': stats,
        'badge_url': badge_url
    }

    # Render Template
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template("TEST_RESULTS.md.j2")
    
    context = {
        'suites': suites,
        'summary': summary_data,
        'build_info': build_info,
        'package_versions': package_versions,
        'generated_at': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    }
    
    rendered_doc = template.render(context)
    
    os.makedirs(DOCS_DIR, exist_ok=True)
    with open(DETAILED_DOC_PATH, "w") as f:
        f.write(rendered_doc)
        
    print(f"Docs generated at: {DETAILED_DOC_PATH}")

    # Optional: Save Summary JSON for other scripts
    os.makedirs(REPORTS_DIR, exist_ok=True)
    with open(SUMMARY_OUTPUT_PATH, "w") as f:
        json.dump({'summary': summary_data, 'build': build_info}, f, indent=4)

if __name__ == "__main__":
    main()