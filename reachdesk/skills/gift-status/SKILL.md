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

## Choosing the right script

Pick the script based on what the user is asking:

| Question type | Script | Why |
|---------------|--------|-----|
| Recipient status, delivery tracking, pending/failed sends | `list_sends.py` | Returns recipient details, send status, delivery info |
| Who sent gifts, sender activity, user/team usage, BDR frequency | `list_transactions.py --types campaign_sends` | Has `created_by.name`, `created_by.email`, and `send.team_name` fields that `list_sends.py` does not |

**When the user asks about "most active users", "who is sending", "BDR usage", "sender breakdown", or any question involving sender identity — go straight to `list_transactions.py --types campaign_sends`. Skip `list_sends.py` entirely.**

## Workflow

### 1. Determine the scope

Ask the user what they want to check:
- A specific date range (e.g. "this week", "last month")
- Recent sends overall (default: last 30 days)

Convert relative dates to YYYY-MM-DD format before running the script.

### 2. Fetch data

**For delivery status questions** — use `list_sends.py`:

```bash
(set -a && source "$ENV_FILE" && set +a && python "$SCRIPTS_DIR/list_sends.py" \
  --start-date <YYYY-MM-DD> \
  --end-date <YYYY-MM-DD> \
  --per-page 50)
```

**For sender/user activity questions** — use `list_transactions.py`:

```bash
(set -a && source "$ENV_FILE" && set +a && python "$SCRIPTS_DIR/list_transactions.py" \
  --types campaign_sends \
  --start-date <YYYY-MM-DD> \
  --end-date <YYYY-MM-DD>)
```

Pagination info is at `data.pagination.total_pages` in the response (not at the top level). Paginate with `--page N` if `total_pages > 1`.

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
- Pagination is at `data.pagination.total_pages`, not at the top level of the JSON response
- `list_transactions.py` with `--types campaign_sends` exposes `created_by.name`, `created_by.email`, and `send.team_name` — use it for any sender-related analysis
