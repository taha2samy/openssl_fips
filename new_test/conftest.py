# conftest.py
import pytest
import subprocess
import shutil
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

def pytest_addoption(parser):
    parser.addoption("--image", action="store", required=True, help="Docker image tag to verify")

@pytest.fixture(scope="session")
def image_tag(request):
    return request.config.getoption("--image")

@pytest.fixture(scope="session")
def run_docker():
    docker_bin = shutil.which("docker")
    
    if not docker_bin:
        standard_paths = ["/usr/bin/docker", "/usr/local/bin/docker"]
        for path in standard_paths:
            if shutil.os.path.exists(path):
                docker_bin = path
                break
    if not docker_bin:
        pytest.fail("Docker executable not found in PATH or standard locations.")

    def _executor(image: str, args: list):
        cmd = ["docker", "run", "--rm", image] + args
        logger.info(f"Executing: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=False, 
                check=False
            )
            stdout_decoded = result.stdout.decode('utf-8', errors='ignore')
            stderr_decoded = result.stderr.decode('utf-8', errors='ignore')
            
            from dataclasses import dataclass
            @dataclass
            class CleanResult:
                returncode: int
                stdout: str
                stderr: str
            
            return CleanResult(result.returncode, stdout_decoded, stderr_decoded)
        except Exception as e:
            pytest.fail(f"Docker command execution failed: {str(e)}")

    return _executor