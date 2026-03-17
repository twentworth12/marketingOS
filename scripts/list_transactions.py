#!/usr/bin/env python3
"""List transactions from Reachdesk.

Usage:
    python list_transactions.py [--start-date YYYY-MM-DD] [--end-date YYYY-MM-DD] \\
        [--types campaign_sends refund] [--states processed pending] \\
        [--currencies USD EUR] [--campaign-types gift_card bundle] \\
        [--page N]
"""

import argparse
import json
from reachdesk import api_request


def main():
    parser = argparse.ArgumentParser(description="List Reachdesk transactions")
    parser.add_argument("--start-date", help="Filter from date (YYYY-MM-DD)")
    parser.add_argument("--end-date", help="Filter until date (YYYY-MM-DD)")
    parser.add_argument("--page", type=int, default=1, help="Page number (default: 1)")
    parser.add_argument("--types", nargs="+",
                        choices=["balance_allocation", "balance_top_up", "campaign_sends",
                                 "contracted_free_credit", "contracted_paid_credit",
                                 "currency_conversion", "free_credit", "other", "refund",
                                 "sourced_items", "upfront_balance_top_up", "warehouse_sends",
                                 "store_portal"],
                        help="Transaction types to include")
    parser.add_argument("--states", nargs="+", choices=["cancelled", "pending", "processed"],
                        help="Transaction states to include")
    parser.add_argument("--currencies", nargs="+",
                        choices=["AUD", "CAD", "DKK", "EUR", "GBP", "INR", "NOK", "SEK", "USD"],
                        help="Currencies to include")
    parser.add_argument("--campaign-types", nargs="+",
                        choices=["bundle", "gift_card", "marketplace", "note"],
                        help="Campaign types to include")
    parser.add_argument("--team-ids", nargs="+", type=int, help="Filter by team IDs")
    parser.add_argument("--user-ids", nargs="+", type=int, help="Filter by user IDs")

    args = parser.parse_args()

    params: dict = {"page": args.page}
    if args.start_date:
        params["start_date"] = args.start_date
    if args.end_date:
        params["end_date"] = args.end_date
    if args.types:
        params["transaction_types[]"] = args.types
    if args.states:
        params["states[]"] = args.states
    if args.currencies:
        params["currencies[]"] = args.currencies
    if args.campaign_types:
        params["campaign_types[]"] = args.campaign_types
    if args.team_ids:
        params["team_ids[]"] = args.team_ids
    if args.user_ids:
        params["user_ids[]"] = args.user_ids

    result = api_request("GET", "/transactions", params=params)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
