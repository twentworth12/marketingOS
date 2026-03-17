---
name: spend-report
description: Generate a gifting spend report from Reachdesk transactions. Use when a marketer wants to understand gifting costs over a period, when reporting on budget usage to a manager, when breaking down spend by campaign type or currency, or when reconciling gifting activity at end of quarter.
argument-hint: "<date range or period, e.g. Q1 2026>"
---

## Overview

Pull Reachdesk transaction data and produce a clear spend summary with breakdowns by campaign type, currency, team, and status.

## Workflow

### 1. Clarify the reporting period

Ask the user for:
- Date range (e.g. "Q1 2026", "last 30 days", "March 2026")
- Any filters: specific currencies, campaign types, teams, or transaction types

Convert relative dates or quarters to YYYY-MM-DD format.

### 2. Fetch transactions

```bash
cd scripts && python list_transactions.py \
  --start-date <YYYY-MM-DD> \
  --end-date <YYYY-MM-DD> \
  [--types campaign_sends] \
  [--states processed] \
  [--currencies USD EUR GBP] \
  [--campaign-types gift_card bundle]
```

Paginate through all pages to get a complete dataset.

### 3. Summarise the spend

Present the report in sections:

**Total spend by currency**
| Currency | Total Amount |
|----------|-------------|
| USD | $X,XXX.XX |
| EUR | €X,XXX.XX |

**Spend by campaign type**
| Type | Count | Total |
|------|-------|-------|
| Gift card | N | $X,XXX |
| Bundle | N | $X,XXX |

**Spend by status**
| Status | Count | Total |
|--------|-------|-------|
| Processed | N | $X,XXX |
| Pending | N | $X,XXX |
| Cancelled | N | $X,XXX |

**Top sends** — list the 5 highest-value sends in the period.

### 4. Add commentary

- Compare to prior period if the user asks
- Flag any unusually large individual transactions
- Note refunds or cancellations that offset spend
- Summarise key takeaways in 2–3 bullet points

## Notes

- Focus on `campaign_sends` transaction type for gifting spend; other types (top-ups, allocations) are accounting movements
- Cancelled transactions reduce net spend — account for them in totals
- If the user wants team-level breakdowns, ask for team IDs and use `--team-ids`
