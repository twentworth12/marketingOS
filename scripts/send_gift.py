#!/usr/bin/env python3
"""Trigger a gift send from a Reachdesk campaign.

Usage:
    python send_gift.py --campaign-id 123 --sender user@company.com \\
        --first-name Jane --last-name Doe --email jane@example.com \\
        [--company "Acme Corp"] [--street "123 Main St"] [--city Boston] \\
        [--state MA] [--zipcode 02101] [--country US] \\
        [--currency USD] [--approved auto] [--no-confirm-address] \\
        [--note "Thanks for the meeting!"]
"""

import argparse
import json
from reachdesk import api_request


def main():
    parser = argparse.ArgumentParser(description="Trigger a Reachdesk campaign send")

    # Required
    parser.add_argument("--campaign-id", type=int, required=True, help="Campaign ID to trigger")
    parser.add_argument("--sender", required=True, help="Sender email (must be a platform user)")

    # Recipient
    parser.add_argument("--first-name", required=True, help="Recipient first name")
    parser.add_argument("--last-name", required=True, help="Recipient last name")
    parser.add_argument("--email", required=True, help="Recipient email")
    parser.add_argument("--company", help="Recipient company name")
    parser.add_argument("--street", help="Street address line 1")
    parser.add_argument("--street2", help="Street address line 2")
    parser.add_argument("--city", help="City")
    parser.add_argument("--state", help="State/province")
    parser.add_argument("--zipcode", help="Zip/postal code")
    parser.add_argument("--country", help="Country code")

    # Options
    parser.add_argument("--currency", choices=["AUD", "CAD", "DKK", "EUR", "GBP", "INR", "NOK", "SEK", "USD"],
                        help="Payment currency")
    parser.add_argument("--wallet-type", choices=["User", "Team"], default="User", help="Wallet type (default: User)")
    parser.add_argument("--team-name", help="Team wallet name (if wallet-type is Team)")
    parser.add_argument("--approved", choices=["true", "false", "auto"], default="auto",
                        help="Approval mode (default: auto)")
    parser.add_argument("--no-confirm-address", action="store_true", help="Skip address confirmation email")
    parser.add_argument("--note", help="Handwritten note text for bundle campaigns")
    parser.add_argument("--request-id", help="Unique request identifier for idempotency")
    parser.add_argument("--source", help="Trigger source name")

    args = parser.parse_args()

    recipient = {
        "first_name": args.first_name,
        "last_name": args.last_name,
        "email": args.email,
    }
    for field, attr in [("company_name", "company"), ("street_address_1", "street"),
                        ("street_address_2", "street2"), ("city", "city"),
                        ("state", "state"), ("zipcode", "zipcode"), ("country", "country")]:
        val = getattr(args, attr, None)
        if val:
            recipient[field] = val

    body: dict = {
        "sender": args.sender,
        "recipient": recipient,
        "approved": args.approved,
    }
    if args.currency:
        body["payment_currency"] = args.currency
    if args.wallet_type:
        body["payment_wallet_type"] = args.wallet_type
    if args.team_name:
        body["team_name"] = args.team_name
    if not args.no_confirm_address:
        body["confirm_address"] = True
    else:
        body["confirm_address"] = False
    if args.note:
        body["bundle_handwritten_note"] = args.note
    if args.request_id:
        body["request_id"] = args.request_id
    if args.source:
        body["source"] = args.source

    result = api_request("POST", f"/campaigns/{args.campaign_id}/trigger", body=body)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
