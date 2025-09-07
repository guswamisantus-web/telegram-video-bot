import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR", "downloads")
ASSETS_DIR = os.getenv("ASSETS_DIR", "assets")
DB_PATH = os.getenv("DB_PATH", "data/bot.db")
DEFAULT_STYLE = os.getenv("DEFAULT_STYLE", "short")

# Ensure folders exist
Path(DOWNLOAD_DIR).mkdir(parents=True, exist_ok=True)
Path(ASSETS_DIR).mkdir(parents=True, exist_ok=True)
Path(os.path.dirname(DB_PATH) or ".").mkdir(parents=True, exist_ok=True)