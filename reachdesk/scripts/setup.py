#!/usr/bin/env python3
"""Save the Reachdesk API token to a shared path that persists across plugin versions.

Directory layout in Cowork:
  .../reachdesk-plugin/          <- _SHARED_ROOT (token lives here)
  └── reachdesk/
      └── <version>/             <- _PLUGIN_ROOT
          └── scripts/
              └── setup.py       <- __file__

Token is saved to _SHARED_ROOT/reachdesk_token.json so it survives
version updates.

Usage:
    python setup.py --token <api_token>
"""

import argparse
import json
from pathlib import Path

# scripts/setup.py → scripts/ → <version>/ → reachdesk/ → reachdesk-plugin/
_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SHARED_ROOT = _PLUGIN_ROOT.parent.parent
_TOKEN_PATH = _SHARED_ROOT / "reachdesk_token.json"


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
