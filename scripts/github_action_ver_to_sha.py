import os
import re
import subprocess
from ruamel.yaml import YAML

def is_sha(text):
    return bool(re.match(r'^[a-fA-F0-9]{40}$', text))

def get_sha(repo, tag):
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{repo}/commits/{tag}", "--jq", ".sha"],
            capture_output=True,
            text=True,
            check=True
        )
        sha = result.stdout.strip()
        return sha if is_sha(sha) else None
    except subprocess.CalledProcessError:
        print(f"   [!] Failed to fetch SHA for {repo}@{tag}")
        return None

def process_steps(steps, yaml_obj):
    updated = False
    if not steps or not isinstance(steps, list):
        return False

    for step in steps:
        uses = step.get('uses')
        if not uses or '@' not in uses or uses.startswith('./'):
            continue
        
        repo, version = uses.split('@', 1)
        
        if is_sha(version):
            continue
        
        print(f"   [*] Fetching SHA for {repo}@{version}...")
        new_sha = get_sha(repo, version)
        
        if new_sha:
            step['uses'] = f"{repo}@{new_sha}"
            print(f"   [+] Updated: {version} -> {new_sha[:7]}")
            updated = True
    return updated

def pin_files(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"\n--- Processing: {file_path} ---")
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f)

    file_updated = False

    if 'jobs' in data:
        for job_name, job_data in data['jobs'].items():
            if isinstance(job_data, dict) and 'steps' in job_data:
                if process_steps(job_data['steps'], yaml):
                    file_updated = True

    elif 'runs' in data and 'steps' in data['runs']:
        if process_steps(data['runs']['steps'], yaml):
            file_updated = True

    if file_updated:
        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)
        print(f"Done! {file_path} updated.")
    else:
        print(f"No changes needed for {file_path}.")

if __name__ == "__main__":
    files_to_pin = [
        ".github/workflows/build.yml",
        ".github/workflows/main.yml",
        ".github/actions/setup-task/action.yml",
        ".github/actions/cleanup-ghcr/action.yml"
    ]
    
    for file in files_to_pin:
        pin_files(file)