---
name: send-gift
description: Send a gift to a contact by triggering a Reachdesk campaign. Use when a marketer wants to send a gift to a prospect or customer, when following up after a meeting or event, or when running an account-based gifting campaign.
argument-hint: "<recipient name or email> [campaign context]"
---

## Overview

Walk the user through sending a Reachdesk gift — identifying the right recipient and campaign, confirming the send details, and triggering the delivery.

## Workflow

### 1. Gather send details

Ask the user for the following if not already provided:
- **Campaign ID** — which Reachdesk campaign to trigger (users can find this in the Reachdesk UI under Campaigns)
- **Recipient** — name, email, and optionally company and address
- **Sender** — the email of the Reachdesk platform user sending the gift (defaults to the user if known)
- **Currency** — payment currency (USD, EUR, GBP, etc.)
- **Note** — optional handwritten note for bundle campaigns

### 2. Look up the recipient (optional)

If the user provides a company name but not a specific contact, search first:

```bash
SCRIPTS_DIR=$(find /mnt -path "*reachdesk*/scripts/list_contacts.py" 2>/dev/null | head -1 | xargs dirname) && python "$SCRIPTS_DIR/list_contacts.py" --account "<company name>"
```

Present matching contacts and let the user confirm which one to send to.

### 3. Confirm before sending

Show a summary of the send before executing:
- Recipient name, email, company
- Campaign ID
- Sender
- Currency and wallet type
- Handwritten note (if any)

Ask the user to confirm before proceeding.

### 4. Trigger the send

```bash
SCRIPTS_DIR=$(find /mnt -path "*reachdesk*/scripts/send_gift.py" 2>/dev/null | head -1 | xargs dirname) && python "$SCRIPTS_DIR/send_gift.py" \
  --campaign-id <id> \
  --sender <sender_email> \
  --first-name <first> \
  --last-name <last> \
  --email <email> \
  [--company "<company>"] \
  [--currency <currency>] \
  [--note "<note>"] \
  [--approved auto]
```

### 5. Report the result

On success, show:
- Send ID
- Status
- Claim URL (if gift card)
- Next steps (e.g. address confirmation email sent to recipient)

On error, explain what went wrong and suggest fixes (invalid campaign ID, sender not a platform user, etc.).

## Notes

- The sender email must belong to an active Reachdesk platform user
- By default, address confirmation is enabled — the recipient will receive an email to confirm their address before the gift ships
- Use `--approved auto` unless the user specifically wants to pre-approve or hold sends
