---
name: reachdesk-setup
description: Connect your Reachdesk account by saving your API token. Use when setting up the plugin for the first time, when your token has expired or been revoked, or when switching to a different Reachdesk account.
argument-hint: "<your Reachdesk API token>"
---

## Overview

Save a Reachdesk API token to the project's `.env` file so all Reachdesk skills can authenticate automatically. The token persists between sessions because it's stored in the local folder attached to this Cowork project.

## Workflow

### 1. Find the project folder

Find the local folder attached to this Cowork project. It's typically mounted under `/mnt/`. List the directories:

```bash
ls /mnt/
```

Identify the user's project directory (not `.local-plugins` or other system mounts). Save this path as `PROJECT_DIR`.

### 2. Get a Reachdesk API token

Tell the user:
- Log into Reachdesk at https://app.reachdesk.com
- Go to **Settings → API Tokens**
- Click **Create Token**, give it a name, and copy the token — it's only shown once

### 3. Ask for the token

Ask the user to paste their API token.

### 4. Save the token

Save it to the `.env` file in the project folder. Find the scripts directory first:

```bash
SCRIPTS_DIR=$(find /mnt -path "*reachdesk*/scripts/setup.py" 2>/dev/null | head -1 | xargs dirname)
python "$SCRIPTS_DIR/setup.py" --token <token> --project-dir <PROJECT_DIR>
```

### 5. Verify it works

```bash
cd <PROJECT_DIR> && python "$SCRIPTS_DIR/list_contacts.py" --per-page 1
```

### 6. Confirm

If successful, tell the user they're connected and ready to start sending gifts. The token is stored in `<PROJECT_DIR>/.env` and will persist between sessions.

If it fails, tell them to double-check their token. If they didn't copy it when it was shown, they'll need to create a new one in Reachdesk.

## Important

- The `.env` file is saved to the user's local project folder, NOT inside the plugin directory
- Make sure to `cd` to the project folder before running other scripts so they can find the `.env` file
- Add `.env` to `.gitignore` if the project folder is a git repo
