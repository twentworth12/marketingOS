#!/usr/bin/env python3
"""Save the Reachdesk API token to the local config file and shell profile.

Usage:
    python setup.py --token <api_token>
"""

import argparse
import json
import os
from pathlib import Path

CONFIG_PATH = Path.home() / ".config" / "reachdesk" / "config.json"
BASHRC_PATH = Path.home() / ".bashrc"
ENV_VAR = "REACHDESK_API_TOKEN"
ENV_MARKER = "# reachdesk-plugin"


def save_to_config(token: str):
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps({"api_token": token}, indent=2))
    CONFIG_PATH.chmod(0o600)
    print(f"Token saved to {CONFIG_PATH}")


def save_to_bashrc(token: str):
    export_line = f'export {ENV_VAR}="{token}"'
    new_block = f"{ENV_MARKER}\n{export_line}\n"

    if BASHRC_PATH.exists():
        contents = BASHRC_PATH.read_text()
        # Replace existing block if present
        if ENV_MARKER in contents:
            lines = contents.splitlines(keepends=True)
            new_lines = []
            skip_next = False
            for line in lines:
                if line.strip() == ENV_MARKER:
                    new_lines.append(new_block)
                    skip_next = True
                elif skip_next and line.strip().startswith(f"export {ENV_VAR}"):
                    skip_next = False
                else:
                    skip_next = False
                    new_lines.append(line)
            BASHRC_PATH.write_text("".join(new_lines))
        else:
            with BASHRC_PATH.open("a") as f:
                f.write(f"\n{new_block}")
    else:
        BASHRC_PATH.write_text(new_block)

    print(f"Token written to {BASHRC_PATH} as ${ENV_VAR}")


def main():
    parser = argparse.ArgumentParser(description="Save Reachdesk API token")
    parser.add_argument("--token", required=True, help="Reachdesk API token")
    args = parser.parse_args()

    save_to_config(args.token)
    save_to_bashrc(args.token)
    print("Done. Token will persist across sessions.")


if __name__ == "__main__":
    main()
