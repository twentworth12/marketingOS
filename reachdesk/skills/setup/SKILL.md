---
name: setup
description: Connect your Reachdesk account by saving your API token. Use when setting up the plugin for the first time, when your token has expired or been revoked, or when switching to a different Reachdesk account.
argument-hint: "<your Reachdesk API token>"
---

## Overview

Save a Reachdesk API token to your machine so all other Reachdesk skills can authenticate automatically.

## Workflow

### 1. Get a Reachdesk API token

Tell the user:
- Log into Reachdesk at https://app.reachdesk.com
- Go to **Settings → API Tokens**
- Click **Create Token**, give it a name, and copy the token — it's only shown once

### 2. Ask for the token

Ask the user to paste their API token.

### 3. Save the token

```bash
cd scripts && python setup.py --token <token>
```

### 4. Verify it works

```bash
cd scripts && python list_contacts.py --per-page 1
```

### 5. Confirm

If successful, tell the user they're connected and ready to start sending gifts.

If it fails, tell them to double-check their token. If they didn't copy it when it was shown, they'll need to create a new one in Reachdesk.
