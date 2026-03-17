# Reachdesk Plugin for Claude Cowork

Send gifts, track deliveries, and manage gifting campaigns — all from Claude Cowork.

## What this plugin does

This plugin connects Claude Cowork to the [Reachdesk](https://reachdesk.com) gifting platform, letting marketers manage gift-sending workflows through conversation rather than switching between tools.

### Skills

| Skill | What it does |
|-------|-------------|
| `send-gift` | Trigger a gift send from a Reachdesk campaign to a contact |
| `gift-status` | Check delivery status of recent sends — what's delivered, pending, or needs attention |
| `browse-contacts` | Search and browse contacts in Reachdesk by company or name |
| `spend-report` | Generate a gifting spend report with breakdowns by campaign type, currency, and team |

### Commands

| Command | What it does |
|---------|-------------|
| `/reachdesk:setup` | Connect your Reachdesk account by saving your API token |

## Getting started

### 1. Install the plugin

1. Open Claude Cowork and click **Customize** in the left sidebar
2. Select **Add marketplace by URL**
3. Enter the following URL and click **Sync**:
   ```
   https://github.com/twentworth12/reachdesk-plugin.git
   ```
4. Once synced, find **Reachdesk** in the marketplace and click **Install**

### 2. Connect your Reachdesk account

Run the setup command in Cowork:

```
/reachdesk:setup
```

Claude will walk you through generating an API token in Reachdesk (Settings → API Tokens) and saving it securely to your machine.

### 3. Start gifting

Use any of the skills by typing `/` in a Cowork conversation, or just describe what you want:

- *"Send a gift to Jane Doe at Acme Corp"*
- *"What gifts are still pending from last week?"*
- *"Show me our gifting spend for Q1"*

## Requirements

- A [Reachdesk](https://reachdesk.com) account with API access
- Claude Cowork (available on Pro, Max, Team, and Enterprise plans)
- Python 3 (available by default in the Cowork environment)

## API token

Your API token is saved locally at `~/.config/reachdesk/config.json` with owner-only read permissions. It is never stored in the plugin directory or committed to version control.

To revoke access, delete the token in Reachdesk under **Settings → API Tokens**, or remove the config file:

```bash
rm ~/.config/reachdesk/config.json
```

## Reachdesk API

This plugin uses the [Reachdesk API v2](https://reachdesk.readme.io/reference/trigger-campaign). The following endpoints are used:

- `POST /campaigns/{id}/trigger` — send a gift
- `GET /sends` — list sends
- `GET /contacts` — list contacts
- `GET /transactions` — list transactions
- `GET /organization` — get org info
- `POST /gdpr/requests` — create GDPR request
- `GET /gdpr/requests/{id}` — get GDPR request status
