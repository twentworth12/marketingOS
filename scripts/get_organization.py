#!/usr/bin/env python3
"""Get organization info from Reachdesk.

Usage:
    python get_organization.py
"""

import json
from reachdesk import api_request


def main():
    result = api_request("GET", "/organization")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
