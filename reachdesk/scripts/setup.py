#!/usr/bin/env python3
"""Save the Reachdesk API token to a .env file in the project folder.

The project folder is the local folder attached to the Cowork project,
which is mounted from the host machine and persists between sessions.

Usage:
    python setup.py --token <api_token> --project-dir /path/to/project
"""

import argparse
from pathlib import Path

ENV_FILE = ".env"


def main():
    parser = argparse.ArgumentParser(description="Save Reachdesk API token")
    parser.add_argument("--token", required=True, help="Reachdesk API token")
    parser.add_argument("--project-dir", required=True, help="Path to the Cowork project folder")
    args = parser.parse_args()

    env_path = Path(args.project_dir) / ENV_FILE
    env_var = f"REACHDESK_API_TOKEN={args.token}"

    # Read existing .env or start fresh
    if env_path.exists():
        lines = env_path.read_text().splitlines()
        # Replace existing token line if present
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
