import json
from pathlib import Path

from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError


class TelegramDownloader:
    def __init__(self, api_id, api_hash, phone, session_name='session'):
        self.client = TelegramClient(session_name, api_id, api_hash)
        self.phone = phone

    def connect(self):
        self.client.connect()
        if not self.client.is_user_authorized():
            print("⚠️ First-time login. A code will be sent to your Telegram.")
            self.client.send_code_request(self.phone)
            code = input("Enter the login code you received in Telegram: ")
            try:
                self.client.sign_in(self.phone, code)
            except SessionPasswordNeededError:
                pwd = input("Two-step verification enabled. Enter your Telegram password: ")
                self.client.sign_in(password=pwd)

    def download_messages(
            self,
            chat_id_or_username,
            out_path,
            limit=10000,
            output_format="txt"
    ):
        chat = self.client.get_entity(chat_id_or_username)
        messages = self.client.get_messages(chat, limit=limit)

        Path(out_path).parent.mkdir(parents=True, exist_ok=True)

        if output_format == "txt":
            with open(out_path, 'w', encoding='utf-8') as f:
                for msg in messages:
                    f.write(f"{msg.sender_id}\t{msg.text or ''}\n")

        elif output_format == "json":
            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump([
                    {
                        "id": msg.id,
                        "sender_id": msg.sender_id,
                        "date": msg.date.isoformat(),
                        "text": msg.text
                    } for msg in messages
                ], f, ensure_ascii=False, indent=2)

        elif output_format == "md":
            with open(out_path, 'w', encoding='utf-8') as f:
                for msg in messages:
                    f.write(
                        f"**{msg.sender_id}** — _{msg.date.strftime('%Y-%m-%d %H:%M')}_\n\n"
                        f"{msg.text or ''}\n\n---\n\n"
                    )

    def close(self):
        self.client.disconnect()
