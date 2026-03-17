#!/usr/bin/env python3
"""List gift sends from Reachdesk.

Usage:
    python list_sends.py [--project-dir DIR] [--start-date YYYY-MM-DD] [--end-date YYYY-MM-DD] [--page N] [--per-page N]
"""

import argparse
import json
from reachdesk import add_project_dir_arg, load_env, api_request


def main():
    parser = argparse.ArgumentParser(description="List Reachdesk sends")
    add_project_dir_arg(parser)
    parser.add_argument("--start-date", help="Filter sends from this date (YYYY-MM-DD)")
    parser.add_argument("--end-date", help="Filter sends before this date (YYYY-MM-DD)")
    parser.add_argument("--start-updated-date", help="Filter by first update date (YYYY-MM-DD)")
    parser.add_argument("--end-updated-date", help="Filter by last update date (YYYY-MM-DD)")
    parser.add_argument("--page", type=int, default=1, help="Page number (default: 1)")
    parser.add_argument("--per-page", type=int, default=25, help="Results per page (default: 25)")
    args = parser.parse_args()
    load_env(args)

    params = {"page": args.page, "per_page": args.per_page}
    if args.start_date:
        params["start_date"] = args.start_date
    if args.end_date:
        params["end_date"] = args.end_date
    if args.start_updated_date:
        params["start_updated_date"] = args.start_updated_date
    if args.end_updated_date:
        params["end_updated_date"] = args.end_updated_date

    result = api_request("GET", "/sends", params=params)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
