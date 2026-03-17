#!/usr/bin/env python3
"""List contacts from Reachdesk.

Usage:
    python list_contacts.py [--project-dir DIR] [--account NAME] [--page N] [--per-page N]
"""

import argparse
import json
from reachdesk import add_project_dir_arg, load_env, api_request


def main():
    parser = argparse.ArgumentParser(description="List Reachdesk contacts")
    add_project_dir_arg(parser)
    parser.add_argument("--account", help="Filter by company/account name")
    parser.add_argument("--page", type=int, default=1, help="Page number (default: 1)")
    parser.add_argument("--per-page", type=int, default=25, help="Results per page (default: 25)")
    args = parser.parse_args()
    load_env(args)

    params = {"page": args.page, "per_page": args.per_page}
    if args.account:
        params["account_name"] = args.account

    result = api_request("GET", "/contacts", params=params)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
