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

# reachdesk.py lives at <plugin_root>/scripts/reachdesk.py
# so plugin root is always two levels up from this file
_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_TOKEN_PATH = _PLUGIN_ROOT / "reachdesk_token.json"


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
        or _load_token_from_file(_TOKEN_PATH)
    )
    if token:
        return token

    print(
        f"Error: Reachdesk API token not found.\n"
        f"Expected token at: {_TOKEN_PATH}\n"
        f"Run the reachdesk-setup skill to connect your account.",
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
