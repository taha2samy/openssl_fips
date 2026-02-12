import os
import sys
from datetime import datetime
from jinja2 import Environment, FileSystemLoader


def env(name: str, default: str | None = None) -> str:
    """
    Helper to read environment variables safely.
    """
    value = os.getenv(name, default)
    if value is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value
with open(os.environ["FIPS_MD_PATH"]) as f:
    fips_table = f.read()

with open(os.environ["UBUNTU_MD_PATH"]) as f:
    ubuntu_table = f.read()


CONTEXT = {
    "project_name": env("PROJECT_NAME"),
    "owner": env("OWNER"),
    "repo_name": env("REPO_NAME"),
    "repo_url": env("REPO_URL"),
    "registry": env("REGISTRY"),
    "core_version": env("CORE_VERSION"),
    "fips_version": env("FIPS_VERSION"),
    "code_repo_name": env("CODE_REPO_NAME"),
    "fips_md": fips_table,
    "ubuntu_md": ubuntu_table,
    "distroless_size": env("DISTROLESS_SIZE"),
    "standard_size": env("STANDARD_SIZE"),
    "generation_date": env(
        "GENERATION_DATE",
        datetime.utcnow().strftime("%Y-%m-%d"),
    ),
    "build_date": env(
        "BUILD_DATE",
        datetime.utcnow().strftime("%Y%m%d"),
    ),
}


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(base_dir)
    template_dir = os.path.join(project_root, "templates")
    output_file = os.path.join(project_root, "README.md")

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
        rendered_content = template.render(CONTEXT)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(rendered_content)

        print(f"README.md successfully generated at: {output_file}")

    except Exception as e:
        print(f"Error generating README: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
