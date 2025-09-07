import logging
from telegram.ext import Application
from . import config
from .handlers import register_handlers

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def main():
    if not config.TELEGRAM_TOKEN:
        raise SystemExit("❌ TELEGRAM_TOKEN missing in .env")
    app = Application.builder().token(config.TELEGRAM_TOKEN).build()
    register_handlers(app)
    log.info("✅ Bot started (polling)...")
    app.run_polling()

if __name__ == "__main__":
    main()