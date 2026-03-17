"""Reachdesk API v2 client.

Token lookup order:
1. REACHDESK_API_TOKEN environment variable
2. .env file in --project-dir (if provided)
3. .env file in the current working directory
4. .env file in common Cowork project mount points (/mnt/*)

Base URL: https://app.reachdesk.com/api/v2
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

BASE_URL = "https://app.reachdesk.com/api/v2"

# Set by load_env() when --project-dir is provided
_project_dir: Path | None = None


def add_project_dir_arg(parser: argparse.ArgumentParser) -> None:
    """Add the --project-dir argument to any script's parser."""
    parser.add_argument(
        "--project-dir",
        help="Path to the project folder containing the .env file",
    )


def load_env(args: argparse.Namespace) -> None:
    """Load the token from the .env file in --project-dir if provided."""
    global _project_dir
    if getattr(args, "project_dir", None):
        _project_dir = Path(args.project_dir)
        token = _load_token_from_env_file(_project_dir / ".env")
        if token:
            os.environ["REACHDESK_API_TOKEN"] = token


def _load_token_from_env_file(path: Path) -> str | None:
    if path.exists():
        try:
            for line in path.read_text().splitlines():
                line = line.strip()
                if line.startswith("REACHDESK_API_TOKEN="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
        except OSError:
            pass
    return None


def _find_token() -> str | None:
    # Check current working directory
    token = _load_token_from_env_file(Path.cwd() / ".env")
    if token:
        return token

    # Check common Cowork project mount points
    for mount in Path("/mnt").iterdir() if Path("/mnt").exists() else []:
        if mount.is_dir():
            token = _load_token_from_env_file(mount / ".env")
            if token:
                return token

    return None


def get_token() -> str:
    token = os.environ.get("REACHDESK_API_TOKEN") or _find_token()
    if token:
        return token

    print(
        "Error: Reachdesk API token not found.\n"
        "Run the reachdesk-setup skill to connect your account.",
        file=sys.stderr,
    )
    sys.exit(1)


def api_request(method: str, path: str, params: dict | None = None, body: dict | None = None) -> dict:
    """Make an authenticated request to the Reachdesk API."""
    url = f"{BASE_URL}{path}"
    if params:
        query = urllib.parse.urlencode(params, doseq=True)
        url = f"{url}?{query}"

    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {get_token()}")
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")

    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode() if e.fp else ""
        print(f"API error {e.code}: {error_body}", file=sys.stderr)
        sys.exit(1)
