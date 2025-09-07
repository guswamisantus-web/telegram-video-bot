import asyncio
from yt_dlp import YoutubeDL
from pathlib import Path
from .utils import safe_name

YDL_OPTS = {
    "outtmpl": "%(title)s.%(ext)s",
    "noplaylist": True,
    "format": "mp4/best",
    "merge_output_format": "mp4",
    "quiet": True,
}

async def download_video(url: str, out_dir: str):
    Path(out_dir).mkdir(parents=True, exist_ok=True)

    def _dl():
        with YoutubeDL({**YDL_OPTS, "outtmpl": str(Path(out_dir) / "%(title)s.%(ext)s")}) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            title = info.get("title") or "Video"
            safe = Path(out_dir) / safe_name(Path(filename).name)
            if Path(filename) != safe:
                Path(filename).rename(safe)
            return str(safe), title

    path, title = await asyncio.to_thread(_dl)
    return {"path": path, "title": title}