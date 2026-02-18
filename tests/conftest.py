import pytest
import subprocess
import shutil
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class CleanResult:
    returncode: int
    stdout: str
    stderr: str

def pytest_addoption(parser):
    parser.addoption("--image", action="store", required=True, help="Docker image tag to verify")

@pytest.fixture(scope="session")
def image_tag(request):
    return request.config.getoption("--image")

@pytest.fixture(scope="session")
def run_docker():
    def _executor(image: str, args: list):
        docker_options = []  
        container_cmd = []  
        
        i = 0
        while i < len(args):
            arg = args[i]
            if arg == "-v" and i + 1 < len(args):
                docker_options.extend(["-v", args[i+1]])
                i += 2
            else:
                container_cmd.append(arg)
                i += 1
        cmd = ["docker", "run", "--user", "0", "--rm"] + docker_options + [image] + container_cmd
        
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
            
            return CleanResult(result.returncode, stdout_decoded, stderr_decoded)
        except Exception as e:
            pytest.fail(f"Local Docker execution failed: {str(e)}")

    return _executor