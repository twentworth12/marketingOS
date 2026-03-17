# Reachdesk Plugin for Claude Cowork

Send gifts, track deliveries, and manage gifting campaigns — all from Claude Cowork.

## What this plugin does

This plugin connects Claude Cowork to the [Reachdesk](https://reachdesk.com) gifting platform, letting marketers manage gift-sending workflows through conversation rather than switching between tools.

### Skills

| Skill | What it does |
|-------|-------------|
| `reachdesk-setup` | Connect your Reachdesk account by saving your API token |
| `send-gift` | Trigger a gift send from a Reachdesk campaign to a contact |
| `gift-status` | Check delivery status of recent sends — what's delivered, pending, or needs attention |
| `browse-contacts` | Search and browse contacts in Reachdesk by company or name |
| `spend-report` | Generate a gifting spend report with breakdowns by campaign type, currency, and team |

## Getting started

### 1. Create a local folder for the plugin

Create a folder on your Mac to store your Reachdesk configuration. This folder will hold your API token in a `.env` file that persists between Cowork sessions.

```bash
mkdir -p ~/reachdesk
```

### 2. Add the folder to your Cowork project

In Claude Cowork, attach the folder you just created as a local folder for your project. This is what allows your token to persist — the folder is mounted from your Mac into the Cowork VM.

### 3. Install the plugin

1. Open Claude Cowork and click **Customize** in the left sidebar
2. Select **Add marketplace by URL**
3. Enter the following URL and click **Sync**:
   ```
   https://github.com/twentworth12/reachdesk-plugin.git
   ```
4. Once synced, find **Reachdesk** in the marketplace and click **Install**

### 4. Connect your Reachdesk account

Run the setup skill in Cowork:

```
/reachdesk-setup
```

Claude will:
1. Ask you to generate an API token in Reachdesk (**Settings → API Tokens**)
2. Save the token to a `.env` file in your local project folder
3. Verify the connection works

### 5. Start gifting

Use any of the skills by typing `/` in a Cowork conversation, or just describe what you want:

- *"Send a gift to Jane Doe at Acme Corp"*
- *"What gifts are still pending from last week?"*
- *"Show me our gifting spend for Q1"*

## How token storage works

Your API token is stored in a `.env` file inside the local folder you attached to your Cowork project. Because this folder lives on your Mac (not inside the ephemeral Cowork VM), the token persists between sessions.

```
~/reachdesk/.env          <- on your Mac, persists forever
  └── REACHDESK_API_TOKEN=your_token_here
```

The `.env` file has owner-only read permissions (`chmod 600`) and is listed in `.gitignore` so it won't be accidentally committed.

To revoke access, delete the token in Reachdesk under **Settings → API Tokens**, or remove the `.env` file:

```bash
rm ~/reachdesk/.env
```

## Requirements

- A [Reachdesk](https://reachdesk.com) account with API access
- Claude Cowork (available on Pro, Max, Team, and Enterprise plans)
- A local folder attached to your Cowork project (for token persistence)
- Python 3 (available by default in the Cowork environment)

## Reachdesk API

This plugin uses the [Reachdesk API v2](https://reachdesk.readme.io/reference/trigger-campaign). The following endpoints are used:

- `POST /campaigns/{id}/trigger` — send a gift
- `GET /sends` — list sends
- `GET /contacts` — list contacts
- `GET /transactions` — list transactions
- `GET /organization` — get org info
- `POST /gdpr/requests` — create GDPR request
- `GET /gdpr/requests/{id}` — get GDPR request status
