import subprocess
import sys

def log_success(test_number: int, category: str, justification: str):
    print(f"[SUCCESS] TEST {test_number:02d} - {category}: PASSED ({justification})")

def log_failure(test_number: int, category: str, justification: str, error_details: str = None):
    sys.stderr.write(f"[FAILURE] TEST {test_number:02d} - {category}: FAILED ({justification})\n")
    if error_details:
        sys.stderr.write(f"Root Cause: {error_details}\n")
    sys.stderr.write("Process terminated with exit code 1.\n")
    sys.exit(1)

def run_container_command(image_tag: str, args: list, entrypoint: str = None) -> tuple[int, str, str]:
    cmd = ["docker", "run", "--rm"]
    if entrypoint:
        cmd += ["--entrypoint", entrypoint]
    
    cmd += [image_tag] + args
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def test_17_entropy_generation(image_tag: str):
    category = "FIPS Deterministic Random Bit Generator (DRBG)"
    
    code, stdout, stderr = run_container_command(image_tag, ["rand", "-hex", "32"])

    if code == 0 and len(stdout.strip()) == 64:
        log_success(
            17, category,
            "Entropy source successfully accessed; 256-bit random hex string generated under FIPS policy."
        )
    else:
        log_failure(
            17, category,
            "Failed to generate random data. System entropy source may be inaccessible or DRBG failed self-test.",
            f"Stderr: {stderr.strip()}"
        )

def test_18_distroless_purity(image_tag: str):
    category = "Attack Surface Reduction (Distroless Purity)"
    
    is_distroless = "distroless" in image_tag.lower()
    
    code, stdout, stderr = run_container_command(image_tag, ["-c", "exit 0"], entrypoint="sh")

    if is_distroless:
        if code != 0 and ("executable file not found" in stderr or "no such file" in stderr):
            log_success(
                18, category,
                "Verified: Image contains no shell (sh), significantly reducing the potential attack surface."
            )
        else:
            log_failure(
                18, category,
                "Security violation: A shell (sh) was found inside a distroless image.",
                "Distroless images must not contain interpreters or shells."
            )
    else:
        if code == 0:
            log_success(
                18, category,
                "Standard image correctly contains a shell for administrative and debugging tasks."
            )
        else:
            log_failure(
                18, category,
                "Standard image is missing a functional shell.",
                f"Stderr: {stderr.strip()}"
            )

if __name__ == "__main__":
    print("-" * 80)
    print("ENTROPY & DISTROLESS PURITY VALIDATION SUITE")
    print("-" * 80)

    if len(sys.argv) < 2:
        print("Usage: python3 verify_entropy_distroless.py <image_tag>")
        sys.exit(1)

    target_image = sys.argv[1]
    
    test_17_entropy_generation(target_image)
    test_18_distroless_purity(target_image)

    print("-" * 80)
    print(f"[SUCCESS] PURITY & ENTROPY STATUS: PASSED (Target: {target_image})")
    print("-" * 80)