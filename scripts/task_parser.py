import subprocess
import re
from typing import Dict, List, Any

def get_task_tree() -> Dict[str, List[Dict[str, str]]]:
    """Executes 'task --list' and parses it into a grouped JSON-like tree."""
    try:
        result = subprocess.run(["task", "--list"], capture_output=True, text=True, check=True)
        lines = result.stdout.splitlines()
        
        tree = {}
        
        for line in lines:
            if not line.strip().startswith("*"):
                continue
                
            match = re.match(r"\*\s+([^:]+):\s+(.*)", line.strip())
            if match:
                full_name = match.group(1).strip()
                description = match.group(2).strip()
                
                if ":" in full_name:
                    namespace = full_name.split(":")[0]
                    task_name = ":".join(full_name.split(":")[1:])
                else:
                    namespace = "General"
                    task_name = full_name
                
                if namespace not in tree:
                    tree[namespace] = []
                    
                tree[namespace].append({
                    "full_name": full_name,
                    "name": task_name,
                    "description": description
                })
        
        return tree
    except Exception as e:
        return {"Error": [{"name": "Parser", "description": str(e)}]}
if __name__ == "__main__":
    print(get_task_tree())