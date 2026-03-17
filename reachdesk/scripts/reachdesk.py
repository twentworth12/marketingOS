"""Reachdesk API v2 client.

Requires REACHDESK_API_TOKEN environment variable.
Base URL: https://app.reachdesk.com/api/v2
"""

import os
import sys
import json
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

BASE_URL = "https://app.reachdesk.com/api/v2"
CONFIG_PATH = Path.home() / ".config" / "reachdesk" / "config.json"


def get_token() -> str:
    # Prefer environment variable (e.g. for CI or advanced users)
    token = os.environ.get("REACHDESK_API_TOKEN")
    if token:
        return token

    # Fall back to config file written by setup.py
    if CONFIG_PATH.exists():
        try:
            config = json.loads(CONFIG_PATH.read_text())
            token = config.get("api_token")
            if token:
                return token
        except (json.JSONDecodeError, OSError):
            pass

    print(
        "Error: Reachdesk API token not found.\n"
        "Run /reachdesk:setup to connect your account.",
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
