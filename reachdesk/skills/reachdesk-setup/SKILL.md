---
name: reachdesk-setup
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

### 3. Determine the plugin root

Find the plugin root by locating this SKILL.md file and going up two directories:

```bash
PLUGIN_ROOT=$(cd "$(dirname "$(find ~ -path '*/reachdesk/skills/reachdesk-setup/SKILL.md' 2>/dev/null | head -1)")/../.." && pwd) && echo "Plugin root: $PLUGIN_ROOT"
```

### 4. Save the token

```bash
CLAUDE_PLUGIN_ROOT="$PLUGIN_ROOT" python "$PLUGIN_ROOT/scripts/setup.py" --token <token>
```

### 5. Verify it works

```bash
CLAUDE_PLUGIN_ROOT="$PLUGIN_ROOT" python "$PLUGIN_ROOT/scripts/list_contacts.py" --per-page 1
```

### 6. Confirm

If successful, tell the user they're connected and ready to start sending gifts.

If it fails, tell them to double-check their token. If they didn't copy it when it was shown, they'll need to create a new one in Reachdesk.
