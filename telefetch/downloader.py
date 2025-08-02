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

    def download_messages(self, chat_id_or_username, out_path, limit=1000):
        chat = self.client.get_entity(chat_id_or_username)
        messages = self.client.get_messages(chat, limit=limit)

        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as f:
            for msg in messages:
                line = f"{msg.sender_id}\t{msg.text or ''}\n"
                f.write(line)

    def close(self):
        self.client.disconnect()
