import logging
import os
import sys

IS_CI = os.getenv("GITHUB_ACTIONS") == "true"

class GithubActionsFormatter(logging.Formatter):
    """Custom formatter to inject GitHub Actions workflow commands."""
    def format(self, record):
        msg = super().format(record)
        if record.levelno == logging.ERROR:
            return f"::error::{msg}"
        if record.levelno == logging.WARNING:
            return f"::warning::{msg}"
        if record.levelno == logging.INFO and getattr(record, "is_notice", False):
            return f"::notice::{msg}"
        return msg

def setup_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    handler = logging.StreamHandler(sys.stdout)
    
    if IS_CI:
        formatter = GithubActionsFormatter("%(message)s")
    else:
        # Local formatting with colors
        formatter = logging.Formatter("\033[34m%(levelname)s:\033[0m %(message)s")
        
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Singleton instance
log = setup_logger("openssl_fips")

def group_start(title: str):
    if IS_CI:
        print(f"::group::{title}", flush=True)
    else:
        print(f"\n\033[1;34m==> {title}\033[0m", flush=True)

def group_end():
    if IS_CI:
        print("::endgroup::", flush=True)

def notice(msg: str):
    log.info(msg, extra={"is_notice": True})