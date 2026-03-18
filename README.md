# marketingOS

A collection of marketing plugins for Claude Cowork.

## Plugins

### Reachdesk

Send gifts, track deliveries, and manage gifting campaigns through [Reachdesk](https://reachdesk.com).

| Skill | What it does |
|-------|-------------|
| `reachdesk-setup` | Connect your Reachdesk account by saving your API token |
| `send-gift` | Trigger a gift send from a Reachdesk campaign to a contact |
| `gift-status` | Check delivery status and sender activity |
| `browse-contacts` | Search and browse contacts by company or name |
| `spend-report` | Generate spend reports by campaign type, currency, and team |

### LinkedIn Ads Manager

Create, manage, and analyze LinkedIn ad campaigns. *(Coming soon)*

## Getting started

### 1. Create a local folder for credentials

Create a folder on your Mac to store API tokens. This folder persists between Cowork sessions.

```bash
mkdir -p ~/marketingOS
```

### 2. Add the folder to your Cowork project

In Claude Cowork, attach the folder as a local folder for your project.

### 3. Install the plugins

1. Open Claude Cowork and click **Customize** in the left sidebar
2. Select **Add marketplace by URL**
3. Enter the following URL and click **Sync**:
   ```
   https://github.com/twentworth12/marketingOS.git
   ```
4. Once synced, install the plugins you want from the marketplace

### 4. Connect your accounts

Each plugin has a setup skill. For Reachdesk:

```
/reachdesk-setup
```

## How token storage works

API tokens are stored in a `.env` file inside the local folder you attached to your Cowork project. Because this folder lives on your Mac (not inside the ephemeral Cowork VM), tokens persist between sessions.

The `.env` file has owner-only read permissions (`chmod 600`) and is listed in `.gitignore` so it won't be accidentally committed.

## Requirements

- Claude Cowork (available on Pro, Max, Team, and Enterprise plans)
- A local folder attached to your Cowork project (for token persistence)
- Python 3 (available by default in the Cowork environment)
