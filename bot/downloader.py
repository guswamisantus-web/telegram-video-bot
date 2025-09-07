# bot/downloader.py
import asyncio
import os
import tempfile
from yt_dlp import YoutubeDL
from bot.utils import log

# Location of cookies file (optional, helps bypass 429 / login required)
COOKIES_FILE = os.getenv("COOKIES_FILE", "cookies.txt")

def _ydl_opts(output_path: str):
    opts = {
        "outtmpl": output_path,
        "format": "bestvideo+bestaudio/best",  # pick best quality available
        "merge_output_format": "mp4",
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "restrictfilenames": True,
        "nocheckcertificate": True,
    }
    # If cookies.txt exists, use it
    if COOKIES_FILE and os.path.exists(COOKIES_FILE):
        opts["cookiefile"] = COOKIES_FILE
        log.info(f"Using cookies file: {COOKIES_FILE}")
    return opts


async def download_video(url: str, workdir: str = None) -> dict:
    """
    Downloads video using yt-dlp.
    Returns dict with {filepath, title, duration, url}.
    """
    workdir = workdir or tempfile.gettempdir()
    os.makedirs(workdir, exist_ok=True)
    output_path = os.path.join(workdir, "%(title).80s.%(ext)s")

    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, _download_sync, url, output_path)
    return result


def _download_sync(url: str, output_path: str) -> dict:
    info_dict = {}
    try:
        with YoutubeDL(_ydl_opts(output_path)) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            info_dict = {
                "filepath": filename,
                "title": info.get("title"),
                "duration": info.get("duration"),
                "url": url,
            }
            log.info(f"Downloaded {info_dict['title']} -> {filename}")
    except Exception as e:
        log.exception(f"Download error for {url}: {e}")
        raise
    return info_dict


if __name__ == "__main__":
    # For quick testing
    import sys
    test_url = sys.argv[1] if len(sys.argv) > 1 else "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    out = asyncio.run(download_video(test_url))
    print(out)