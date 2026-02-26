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
        print(f"Failed to fetch SHA for {repo}@{tag} using gh cli")
        return None

def pin_github_actions(yaml_file):
    if not os.path.exists(yaml_file):
        print(f"File not found: {yaml_file}")
        return

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.load(f)

    updated = False

    for job_name, job_data in data.get('jobs', {}).items():
        if not isinstance(job_data, dict):
            continue
            
        for step in job_data.get('steps', []):
            uses = step.get('uses')
            if not uses or '@' not in uses:
                continue
            
            repo, version = uses.split('@', 1)
            
            if is_sha(version):
                print(f"Skipping: {repo} (Already uses SHA)")
                continue
            
            new_sha = get_sha(repo, version)
            if new_sha:
                step['uses'] = f"{repo}@{new_sha}"
                step.yaml_add_eol_comment(version, 'uses')
                print(f"Updated:  {repo} | {version} -> {new_sha}")
                updated = True

    if updated:
        with open(yaml_file, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)
        print(f"Done! File updated: {yaml_file}\n")

if __name__ == "__main__":
    workflows = [
        ".github/workflows/build.yml",
        ".github/workflows/main.yml"
    ]
    
    for wf in workflows:
        pin_github_actions(wf)