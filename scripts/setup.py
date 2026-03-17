#!/usr/bin/env python3
"""Save the Reachdesk API token to the local config file.

Usage:
    python setup.py --token <api_token>
"""

import argparse
import json
import os
from pathlib import Path

CONFIG_PATH = Path.home() / ".config" / "reachdesk" / "config.json"


def main():
    parser = argparse.ArgumentParser(description="Save Reachdesk API token")
    parser.add_argument("--token", required=True, help="Reachdesk API token")
    args = parser.parse_args()

    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    config = {"api_token": args.token}
    CONFIG_PATH.write_text(json.dumps(config, indent=2))
    CONFIG_PATH.chmod(0o600)  # owner read/write only

    print(f"Token saved to {CONFIG_PATH}")


if __name__ == "__main__":
    main()
