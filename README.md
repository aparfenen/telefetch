# telefetch
[![Release](https://img.shields.io/github/v/release/aparfenen/telefetch)](https://github.com/aparfenen/telefetch/releases)
[![License](https://img.shields.io/github/license/aparfenen/telefetch)](https://github.com/aparfenen/telefetch/blob/main/LICENSE)
  
Minimal command-line tool for downloading Telegram messages via Telethon.


## Install
```
git clone https://github.com/aparfenen/telefetch.git
cd telefetch
pip install -e .
```

---

## Usage
```
telefetch \
  --api-id <API_ID> \            # Your Telegram API ID (get from https://my.telegram.org)
  --api-hash <API_HASH> \        # Your Telegram API Hash
  --phone <PHONE> \              # Your phone number linked to Telegram (e.g. +12345678901)
  --chat <CHAT> \                # Target chat: @username, group/channel name, or numeric ID
  --out messages.txt \           # Output file path
  --limit 1000 \                 # Max number of messages to fetch (default: 10000)
  --format txt|json|md \         # Output format (default: txt)
  --min-date YYYY-MM-DD \        # (optional) Earliest date to include
  --max-date YYYY-MM-DD          # (optional) Latest date to include
```

---

## Options explained

### Date filtering
Use `--min-date` and `--max-date` (format: `YYYY-MM-DD`) to limit the message range:
- `--min-date YYYY-MM-DD`: include only messages on or after this date  
- `--max-date YYYY-MM-DD`: include only messages on or before this date

### Output formats
- `txt`: plain text, tab-separated  
- `json`: structured JSON with metadata  
- `md`: readable Markdown (sender, date, text)

### First-Time Login
On your first run, Telethon will:  
- Send you a login code via the official Telegram app.
- If 2FA (two-step verification) is enabled, ask for your Telegram password.
- A .session file will be created so you won’t need to log in again.

---

## Example
```bash
telefetch \
  --api-id 123456 \
  --api-hash abcd1234efgh5678 \
  --phone +15551234567 \
  --chat @examplechannel \
  --out ./messages/output.json \
  --limit 500 \
  --format json \
  --min-date 2025-01-01 \
  --max-date 2025-03-01
```
