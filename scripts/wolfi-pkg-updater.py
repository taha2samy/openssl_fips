#!/usr/bin/env python3

import subprocess
import sys
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(ROOT_DIR)

from scripts.logger import log, group_start, group_end, notice

PACKAGES_TO_CHECK = [
    # build / core
    "build-base",
    "perl",
    "linux-headers",
    "wget",
    "ca-certificates",
    
    # runtime
    "libstdc++",
    "zlib",
    "tzdata",
    "posix-libc-utils",
    
    "pkgconf",
    "pcre-dev",
    "zlib-dev",
    "bash",
    "curl",
    "jq",
    "unzip",

    "apk-tools",
    "busybox",
    "glibc",
    "glibc-locale-posix",
    "ld-linux",
    "libcrypt1",
    "libxcrypt",
    "libgcc",
    "wolfi-base",
    "wolfi-baselayout",
    "wolfi-keys"
]

IMAGES_TO_CHECK = {
    "BASE_IMAGE": "cgr.dev/chainguard/wolfi-base:latest",
    "STATIC_IMAGE": "cgr.dev/chainguard/static:latest"
}

OUTPUT_HCL_FILE = os.path.join(ROOT_DIR, "versions.hcl")


def run_command(command_list):
    return subprocess.run(command_list, capture_output=True, text=True, check=True)


def pull_image(image_tag):
    log.info(f"Pulling image: {image_tag}")
    try:
        run_command(["docker", "pull", image_tag])
        log.info(f"Pull successful: {image_tag}")
    except subprocess.CalledProcessError as e:
        log.error(f"Error pulling {image_tag}: {e.stderr}")
        sys.exit(1)


def get_image_digest(image_tag):
    log.info(f"Getting digest for: {image_tag}")
    try:
        result = run_command([
            "docker", "inspect",
            "--format={{index .RepoDigests 0}}",
            image_tag
        ])
        return result.stdout.strip()
    except Exception as e:
        log.error(f"Error getting digest for {image_tag}: {e}")
        return None


def get_latest_package_version(base_image, package_name):
    command = f"apk update > /dev/null && apk search -x {package_name}"
    try:
        result = subprocess.run(
            ["docker", "run", "--rm", base_image, "sh", "-c", command],
            capture_output=True,
            text=True,
            check=True,
            timeout=60
        )

        full_package_string = result.stdout.strip()

        if not full_package_string:
            return None

        full_package_string = full_package_string.split('\n')[0].strip()

        prefix = f"{package_name}-"

        if full_package_string.startswith(prefix):
            return full_package_string[len(prefix):]

        return None

    except Exception:
        return None


def generate_hcl_file(package_versions: dict, image_digests: dict):
    log.info(f"Generating HCL file: {OUTPUT_HCL_FILE}")

    header = f"""# This file is auto-generated. DO NOT EDIT MANUALLY.
"""

    content = header
    content += "\n# --- Base Images (Pinned by Digest) ---\n"

    for var_name, digest in image_digests.items():
        content += f'variable "{var_name}" {{\n  default = "{digest}"\n}}\n'

    content += "\n# --- Package Versions ---\n"

    for package, version in package_versions.items():
        clean_name = package.upper().replace("-", "_").replace("+", "_PLUS")
        variable_name = f"{clean_name}_VER"
        content += f'variable "{variable_name}" {{\n  default = "{version}"\n}}\n'

    with open(OUTPUT_HCL_FILE, "w") as f:
        f.write(content.strip() + "\n")

    notice(f"Successfully wrote to {OUTPUT_HCL_FILE}")


def main():
    group_start("Wolfi Infrastructure Sync")
    image_digests = {}

    for var_name, tag in IMAGES_TO_CHECK.items():
        pull_image(tag)
        digest = get_image_digest(tag)

        if digest:
            image_digests[var_name] = digest
        else:
            sys.exit(1)
    group_end()

    group_start("Upstream Package Discovery")
    base_image_with_digest = image_digests["BASE_IMAGE"]
    package_versions = {}

    for pkg in PACKAGES_TO_CHECK:
        log.info(f"Checking package: {pkg}")
        version = get_latest_package_version(base_image_with_digest, pkg)

        if version:
            package_versions[pkg] = version
        else:
            log.error(f"Error checking package {pkg}")
            sys.exit(1)
    group_end()

    group_start("Manifest Generation")
    generate_hcl_file(package_versions, image_digests)
    group_end()


if __name__ == "__main__":
    main()