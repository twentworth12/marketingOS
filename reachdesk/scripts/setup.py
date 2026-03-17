#!/usr/bin/env python3
"""Save the Reachdesk API token to persistent storage.

Tries multiple locations in order of persistence likelihood:
1. ~/.claude/reachdesk.json  (Claude's own directory, likely host-mounted)
2. ~/.config/reachdesk/config.json  (fallback)
3. ~/.bashrc  (env var for shell sessions)

Usage:
    python setup.py --token <api_token>
"""

import argparse
import json
import os
from pathlib import Path

ENV_VAR = "REACHDESK_API_TOKEN"


def get_token_path() -> Path:
    plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT")
    if plugin_root:
        return Path(plugin_root) / "reachdesk_token.json"
    # Fallback for running outside of Cowork (e.g. local testing)
    return Path.home() / ".config" / "reachdesk" / "config.json"


def main():
    parser = argparse.ArgumentParser(description="Save Reachdesk API token")
    parser.add_argument("--token", required=True, help="Reachdesk API token")
    args = parser.parse_args()

    token_path = get_token_path()
    token_path.parent.mkdir(parents=True, exist_ok=True)
    token_path.write_text(json.dumps({"api_token": args.token}, indent=2))
    token_path.chmod(0o600)

    print(f"Token saved to {token_path}")
    print("Done.")


if __name__ == "__main__":
    main()
