import random

TEMPLATES = {
    "short": [
        "🔥 {title}\n\n#viral #trending #shorts #reels #fyp",
        "🚀 Must-watch: {title}\n\n#viral #now #video #wow",
    ],
}

def make_caption(title: str, style: str = "short"):
    bank = TEMPLATES.get(style, TEMPLATES["short"])
    tpl = random.choice(bank)
    return tpl.format(title=title)