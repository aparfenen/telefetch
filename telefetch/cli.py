import argparse
from telefetch.downloader import TelegramDownloader


def main():
    parser = argparse.ArgumentParser(description="Download Telegram messages.")
    parser.add_argument("--api-id", required=True)
    parser.add_argument("--api-hash", required=True)
    parser.add_argument("--phone", required=True)
    parser.add_argument("--chat", required=True, help="Username or chat ID")
    parser.add_argument("--out", required=True, help="Output .txt file")
    parser.add_argument("--limit", type=int, default=1000)

    args = parser.parse_args()

    dl = TelegramDownloader(args.api_id, args.api_hash, args.phone)
    dl.connect()
    dl.download_messages(args.chat, args.out, args.limit)
    dl.close()
