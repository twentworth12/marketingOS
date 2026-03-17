#!/usr/bin/env python3
"""Save the Reachdesk API token to the plugin directory.

setup.py lives at <plugin_root>/scripts/setup.py, so the token
is always saved to <plugin_root>/reachdesk_token.json — the same
location reachdesk.py looks for it.

Usage:
    python setup.py --token <api_token>
"""

import argparse
import json
from pathlib import Path

# setup.py lives at <plugin_root>/scripts/setup.py
_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_TOKEN_PATH = _PLUGIN_ROOT / "reachdesk_token.json"


def main():
    parser = argparse.ArgumentParser(description="Save Reachdesk API token")
    parser.add_argument("--token", required=True, help="Reachdesk API token")
    args = parser.parse_args()

    _TOKEN_PATH.parent.mkdir(parents=True, exist_ok=True)
    _TOKEN_PATH.write_text(json.dumps({"api_token": args.token}, indent=2))
    _TOKEN_PATH.chmod(0o600)

    print(f"Token saved to {_TOKEN_PATH}")
    print("Done.")


if __name__ == "__main__":
    main()
