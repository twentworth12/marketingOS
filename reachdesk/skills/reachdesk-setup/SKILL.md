---
name: reachdesk-setup
description: Connect your Reachdesk account by saving your API token. Use when setting up the plugin for the first time, when your token has expired or been revoked, or when switching to a different Reachdesk account.
argument-hint: "<your Reachdesk API token>"
---

## Overview

Save a Reachdesk API token so all Reachdesk skills can authenticate. The token is stored in a `.env` file in the local folder attached to this Cowork project, so it persists between sessions.

## Workflow

### 1. Ask for the token

Always ask the user to paste their Reachdesk API token. If they don't have one yet, tell them:
- Log into Reachdesk at https://app.reachdesk.com
- Go to **Settings → API Tokens**
- Click **Create Token**, give it a name, and copy the token — it's only shown once

### 2. Find the project folder

Find the local folder attached to this Cowork project. List directories under `/mnt/`:

```bash
ls /mnt/
```

Identify the user's project directory (not `.local-plugins` or other system mounts). Save this path as `PROJECT_DIR`.

### 3. Save the token

Pipe the token via stdin so it doesn't appear in the process list or shell history:

```bash
SCRIPTS_DIR=$(find /mnt -path "*reachdesk*/scripts/setup.py" 2>/dev/null | head -1 | xargs dirname)
echo "<token>" | python "$SCRIPTS_DIR/setup.py" --project-dir <PROJECT_DIR>
```

### 4. Verify it works

```bash
(set -a && source <PROJECT_DIR>/.env && set +a && python "$SCRIPTS_DIR/list_contacts.py" --per-page 1)
```

### 5. Confirm

If successful, tell the user they're connected and ready to start sending gifts.

If it fails, tell them to double-check their token. If they didn't copy it when it was shown, they'll need to create a new one in Reachdesk.
