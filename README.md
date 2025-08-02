# telefetch
[![Release](https://img.shields.io/github/v/release/aparfenen/telefetch)](https://github.com/aparfenen/telefetch/releases)
[![License](https://img.shields.io/github/license/aparfenen/telefetch)](https://github.com/aparfenen/telefetch/blob/main/LICENSE)
  
Minimal command-line tool for downloading Telegram messages using the Telethon library.
Fetch Telegram messages fast and easy using Telethon.  


## Install
```
git clone https://github.com/aparfenen/telefetch.git
cd telefetch
pip install -e .
```

## Usage
```
telefetch \
  --api-id <API_ID> \          # Your Telegram API ID (get from https://my.telegram.org)
  --api-hash <API_HASH> \      # Your Telegram API Hash
  --phone <PHONE> \            # Your phone number linked to Telegram (e.g. +12345678901)
  --chat <CHAT> \              # Target chat: @username, group/channel name, or numeric ID
  --out messages.txt \         # Output file path
  --limit 1000                  # Max number of messages to fetch (default: 1000)
```

### First-Time Login
On your first run, Telethon will:  
- Send you a login code via the official Telegram app.
- If 2FA (two-step verification) is enabled, ask for your Telegram password.
- A .session file will be created so you won’t need to log in again.

### Example
```
telefetch \
  --api-id 123456 \
  --api-hash abcd1234efgh5678 \
  --phone +15551234567 \
  --chat @examplechannel \
  --out ./messages/output.txt \
  --limit 500
```
