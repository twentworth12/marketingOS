---
name: reachdesk-setup
description: Connect your Reachdesk account by saving your API token. Use when setting up the plugin for the first time, when your token has expired or been revoked, or when switching to a different Reachdesk account.
argument-hint: "<your Reachdesk API token>"
---

## Overview

Save a Reachdesk API token so all Reachdesk skills can authenticate. The token is stored in a `.env` file in the local folder attached to this Cowork project, so it persists between sessions.

**SECURITY: Never set REACHDESK_API_TOKEN inline in a bash command. The raw token value must never appear in any command visible in the chat transcript.**

## Workflow

### 1. Find the project folder

Identify the user's project directory. List available mounts or use the known workspace path:

```bash
ls /mnt/
```

Identify the user's project directory (not `.local-plugins` or other system mounts). Save this path as `PROJECT_DIR`.

### 2. Check for an existing token

Before asking the user for anything, check if a token already exists:

```bash
grep -s "REACHDESK_API_TOKEN=" "$PROJECT_DIR/.env"
```

If `REACHDESK_API_TOKEN` is present and non-empty, **skip straight to step 5 (Verify)** — do not ask the user for a token.

### 3. Ask for the token

Only if the token is missing or empty. Ask the user to paste their Reachdesk API token. If they don't have one yet, tell them:
- Log into Reachdesk at https://app.reachdesk.com
- Go to **Settings → API Tokens**
- Click **Create Token**, give it a name, and copy the token — it's only shown once

### 4. Save the token

Find the setup script relative to the project directory, then pipe the token via stdin:

```bash
SCRIPTS_DIR=$(find "$PROJECT_DIR" -path "*reachdesk*/scripts/setup.py" 2>/dev/null | head -1 | xargs dirname)
echo "<token>" | python "$SCRIPTS_DIR/setup.py" --project-dir "$PROJECT_DIR"
```

### 5. Verify it works

```bash
SCRIPTS_DIR=$(find "$PROJECT_DIR" -path "*reachdesk*/scripts/list_contacts.py" 2>/dev/null | head -1 | xargs dirname)
(set -a && source "$PROJECT_DIR/.env" && set +a && python "$SCRIPTS_DIR/list_contacts.py" --per-page 1)
```

### 6. Confirm

If successful, tell the user they're connected and ready to start sending gifts.

If it fails, tell them to double-check their token. If they didn't copy it when it was shown, they'll need to create a new one in Reachdesk.
