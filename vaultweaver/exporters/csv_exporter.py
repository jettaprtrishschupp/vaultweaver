import os, csv
from ..graph.build import load_index

ROOT = os.path.dirname(os.path.dirname(__file__))
BASE = os.path.dirname(ROOT)
REPORTS_DIR = os.path.join(BASE, "reports")


# --- snippet: safe_join ---

# --- snippet: top_tags ---
def top_tags(index: dict, n: int = 10):
    from collections import Counter
    c = Counter()
    for meta in index.values():
        c.update(meta.get("tags", []))
    return c.most_common(n)
# --- endsnippet ---

def safe_join(base: str, *parts: str) -> str:
    import os
    return os.path.normpath(os.path.join(base, *parts))
# --- endsnippet ---

def export_tags_csv() -> str:
    os.makedirs(REPORTS_DIR, exist_ok=True)
    idx = load_index()
    p = os.path.join(REPORTS_DIR, "tags.csv")
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["file", "tags"])
        for fn, meta in idx.items():
            w.writerow([fn, ",".join(meta.get("tags", []))])
    return p

# --- snippet: clamp_len ---
def clamp_len(s: str, n: int = 280) -> str:
    return s if len(s) <= n else s[:n-1] + "…"
# --- endsnippet ---


# --- snippet: normalize_title ---
def normalize_title(title: str) -> str:
    return " ".join(title.strip().split())
# --- endsnippet ---

