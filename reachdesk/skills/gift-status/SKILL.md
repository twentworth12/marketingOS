---
name: gift-status
description: Check the delivery status of recent gift sends in Reachdesk. Use when a marketer wants to know what's been sent recently, when following up on a specific send, when checking which gifts are pending or delivered, or when auditing sends for a campaign or time period.
argument-hint: "<date range or contact name>"
---

## Overview

Fetch recent Reachdesk sends and give the user a clear status summary — what's delivered, what's pending, and what needs attention.

## Before you start

Find the user's project folder (the local folder attached to this Cowork project, typically under `/mnt/`). Check if it contains a `.env` file with `REACHDESK_API_TOKEN`. If the token is missing, ask the user to paste their Reachdesk API token and run the `reachdesk-setup` skill before continuing.

Find the scripts directory:

```bash
ENV_FILE=$(find /mnt -name ".env" -not -path "*/.local-plugins/*" 2>/dev/null | head -1)
SCRIPTS_DIR=$(find /mnt -path "*reachdesk*/scripts/list_sends.py" 2>/dev/null | head -1 | xargs dirname)
echo "ENV_FILE=$ENV_FILE SCRIPTS_DIR=$SCRIPTS_DIR"
```

**SECURITY: Never set REACHDESK_API_TOKEN inline in a bash command. Always load credentials by sourcing the .env file as shown below. The raw token value must never appear in any command visible in the chat transcript.**

## Workflow

### 1. Determine the scope

Ask the user what they want to check:
- A specific date range (e.g. "this week", "last month")
- Recent sends overall (default: last 30 days)

Convert relative dates to YYYY-MM-DD format before running the script.

### 2. Fetch sends

```bash
(set -a && source "$ENV_FILE" && set +a && python "$SCRIPTS_DIR/list_sends.py" \
  --start-date <YYYY-MM-DD> \
  --end-date <YYYY-MM-DD> \
  --per-page 50)
```

Paginate if `total_pages > 1`.

### 3. Summarise the results

Group sends by status and present a clear overview:

| Status | Count |
|--------|-------|
| Delivered | N |
| Pending | N |
| Awaiting address | N |
| Failed / Cancelled | N |

Then list individual sends with: recipient name, email, campaign name, status, and date sent.

### 4. Highlight anything needing attention

Flag:
- Sends pending for more than 7 days
- Sends where address confirmation hasn't been completed
- Failed or cancelled sends

Offer to help the marketer follow up or resend where relevant.

## Notes

- Default to the last 30 days if no date range is specified
- Use `--per-page 50` to reduce pagination for typical workloads
- Sends are returned in reverse chronological order
