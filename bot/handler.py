import os
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes
from .downloader import download_video
from .generator import make_caption
from .config import DOWNLOAD_DIR
from .utils import file_size

def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Send a video link (YouTube/IG/FB) and I'll download + caption it.")

async def help_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start - intro\nSend a video link to process.")

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = (update.message.text or "").strip()
    if not url.startswith("http"):
        await update.message.reply_text("⚠️ Please send a valid video link.")
        return

    await update.message.reply_text("⏳ Downloading...")
    try:
        result = await download_video(url, DOWNLOAD_DIR)
        path, title = result["path"], result["title"]
        caption = make_caption(title)

        size = file_size(path)
        if size > 2_000_000_000:  # 2GB limit
            await update.message.reply_text("⚠️ File too large for Telegram.")
            return

        with open(path, "rb") as f:
            await update.message.reply_video(video=f, caption=caption)
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}") 