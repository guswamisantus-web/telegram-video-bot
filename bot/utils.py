import os, re, logging

def safe_name(name: str) -> str:
    name = re.sub(r"[^\w\s.-]", "_", name)
    return re.sub(r"\s+", "_", name).strip("_")

def file_size(path: str) -> int:
    return os.path.getsize(path)

log = logging.getLogger("bot")