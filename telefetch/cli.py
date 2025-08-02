import argparse
from datetime import datetime

from telefetch.downloader import TelegramDownloader


def main():
    parser = argparse.ArgumentParser(description="Download Telegram messages.")
    parser.add_argument("--api-id", required=True)
    parser.add_argument("--api-hash", required=True)
    parser.add_argument("--phone", required=True)
    parser.add_argument("--chat", required=True, help="Username or chat ID")
    parser.add_argument("--out", required=True, help="Output .txt file")
    parser.add_argument("--limit", type=int, default=10000)
    parser.add_argument("--format", choices=["txt", "json", "md"], default="txt",
                        help="Output format: txt (default), json, or md")
    parser.add_argument("--min-date", type=lambda d: datetime.strptime(d, "%Y-%m-%d").date(),
                        help="Only include messages on or after this date (YYYY-MM-DD)")
    parser.add_argument("--max-date", type=lambda d: datetime.strptime(d, "%Y-%m-%d").date(),
                        help="Only include messages on or before this date (YYYY-MM-DD)")

    args = parser.parse_args()

    dl = TelegramDownloader(args.api_id, args.api_hash, args.phone)
    dl.connect()
    dl.download_messages(
        args.chat,
        args.out,
        args.limit,
        output_format=args.format,
        min_date=args.min_date,
        max_date=args.max_date
    )
    dl.close()
