---
name: browse-contacts
description: Browse and search contacts in Reachdesk. Use when a marketer wants to find someone to send a gift to, when looking up contacts at a specific company, or when building a list of recipients for a gifting campaign.
argument-hint: "<company name or contact name>"
---

## Overview

Search and browse the Reachdesk contacts list to help the user find the right people to send gifts to.

## Workflow

### 1. Get the search criteria

Ask the user what they're looking for:
- A specific company/account name
- A contact name (note: the API filters by account name, so search by company first)
- All contacts (paginated)

### 2. Fetch contacts

```bash
cd scripts && python list_contacts.py --account "<company name>" --per-page 25
```

Or for all contacts:

```bash
cd scripts && python list_contacts.py --per-page 25 --page 1
```

### 3. Present results

Display contacts in a clean table:

| Name | Email | Title | Company | Country |
|------|-------|-------|---------|---------|

If there are multiple pages, offer to load more.

### 4. Help the user act

After finding contacts, offer next steps:
- Send a gift to one of them (hand off to the send-gift skill)
- Export the list as a summary
- Refine the search (different company, different page)

## Notes

- The API filters by `account_name` (company), not by individual contact name — search by company then scan the results
- If the user knows a contact by name but not company, search for the company name first or browse all contacts
- Results default to 25 per page; use `--per-page` up to the API's limit for larger pulls
