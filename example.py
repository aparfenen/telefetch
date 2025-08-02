from telefetch.downloader import TelegramDownloader

downloader = TelegramDownloader(
    api_id='YOUR_API_ID',
    api_hash='YOUR_API_HASH',
    phone='+123456789'
)

downloader.connect()
downloader.download_messages(
    chat_id_or_username='@your_channel_or_user',
    out_path='messages/output.txt',
    limit=100
)
downloader.close()
