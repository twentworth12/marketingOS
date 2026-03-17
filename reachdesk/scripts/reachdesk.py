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


def _get_token_path() -> Path:
    plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT")
    if plugin_root:
        return Path(plugin_root) / "reachdesk_token.json"
    return Path.home() / ".config" / "reachdesk" / "config.json"


def _load_token_from_file(path: Path) -> str | None:
    if path.exists():
        try:
            return json.loads(path.read_text()).get("api_token")
        except (json.JSONDecodeError, OSError):
            pass
    return None


def get_token() -> str:
    token = (
        os.environ.get("REACHDESK_API_TOKEN")
        or _load_token_from_file(_get_token_path())
    )
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
