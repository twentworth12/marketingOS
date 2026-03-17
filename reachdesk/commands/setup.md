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

4. Confirm the token is working by fetching their org:

```bash
cd scripts && python get_organization.py
```

5. If successful, show the organisation name and tell the user they're ready to start sending gifts.

6. If it fails, tell the user to double-check their token and try again. Remind them the token is only shown once in the Reachdesk UI — if they didn't copy it, they'll need to create a new one.
