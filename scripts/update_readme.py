import os
import sys
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

CONTEXT = {
    "project_name": "Wolfi OpenSSL FIPS Images",
    "owner": "taha2samy",
    "repo_name": "wolfi-openssl-fips",
    "registry": "ghcr.io",
    "core_version": "3.4.0",
    "fips_version": "3.1.2",
    "repo_url": "https://github.com/taha2samy/wolfi-openssl-fips",
    "generation_date": datetime.now().strftime("%Y-%m-%d")
}

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(base_dir)
    template_dir = os.path.join(project_root, 'templates')
    output_file = os.path.join(project_root, 'README.md')

    if not os.path.exists(template_dir):
        print(f"Error: Template directory not found at {template_dir}")
        sys.exit(1)

    try:
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template('README.md.j2')
        
        rendered_content = template.render(CONTEXT)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(rendered_content)
            
        print(f"README.md successfully generated at: {output_file}")
        
    except Exception as e:
        print(f"Error generating README: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()