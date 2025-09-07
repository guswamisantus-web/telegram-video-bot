# Telegram Video Bot (Termux-friendly)

Free, Termux-ready Telegram bot to:
- Download videos from YouTube/IG/FB/etc (yt-dlp)
- Generate simple captions + hashtags
- Create thumbnails and compress for WhatsApp/IG
- Cache repeated URLs and rate-limit users
- Zero-cost stack: python-telegram-bot + FFmpeg + SQLite

## Quick Start (Termux)
```bash
pkg update && pkg upgrade -y
pkg install python ffmpeg git -y
pip install -r requirements.txt
cp .env.example .env    # put your bot token
python -m bot.main