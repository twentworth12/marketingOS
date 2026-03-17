#!/usr/bin/env python3
"""Save the Reachdesk API token to a .env file in the project folder.

The token is read from stdin to avoid exposing it in process lists
or shell history.

Usage:
    echo "your_token" | python setup.py --project-dir /path/to/project
"""

import argparse
import sys
from pathlib import Path

ENV_FILE = ".env"


def main():
    parser = argparse.ArgumentParser(description="Save Reachdesk API token")
    parser.add_argument("--project-dir", required=True, help="Path to the Cowork project folder")
    args = parser.parse_args()

    token = sys.stdin.read().strip()
    if not token:
        print("Error: no token provided on stdin.", file=sys.stderr)
        sys.exit(1)

    env_path = Path(args.project_dir) / ENV_FILE
    env_var = f"REACHDESK_API_TOKEN={token}"

    # Read existing .env or start fresh
    if env_path.exists():
        lines = env_path.read_text().splitlines()
        new_lines = [l for l in lines if not l.startswith("REACHDESK_API_TOKEN=")]
        new_lines.append(env_var)
    else:
        new_lines = [env_var]

    env_path.write_text("\n".join(new_lines) + "\n")
    env_path.chmod(0o600)

    print(f"Token saved to {env_path}")
    print("Done.")


if __name__ == "__main__":
    main()
