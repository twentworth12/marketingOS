name: setup
description: Connect your Reachdesk account by saving your API token. Run this once before using any other Reachdesk skills.

## Instructions

1. Tell the user they need a Reachdesk API token and where to get one:
   - Log into Reachdesk at https://app.reachdesk.com
   - Go to **Settings → API Tokens**
   - Click **Create Token**, give it a name, and copy the token (it's only shown once)

2. Ask the user to paste their API token.

3. Save it by running:

```bash
cd scripts && python setup.py --token <token>
```

4. Confirm the token is working by fetching their contacts:

```bash
cd scripts && python list_contacts.py --per-page 1
```

5. If successful, tell the user they're connected and ready to start sending gifts.

6. If it fails, tell the user to double-check their token and try again. Remind them the token is only shown once in the Reachdesk UI — if they didn't copy it, they'll need to create a new one.
