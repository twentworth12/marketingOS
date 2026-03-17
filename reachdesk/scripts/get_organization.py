#!/usr/bin/env python3
"""Get organization info from Reachdesk.

Usage:
    python get_organization.py [--project-dir DIR]
"""

import argparse
import json
from reachdesk import add_project_dir_arg, load_env, api_request


def main():
    parser = argparse.ArgumentParser(description="Get Reachdesk organization info")
    add_project_dir_arg(parser)
    args = parser.parse_args()
    load_env(args)

    result = api_request("GET", "/organization")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
