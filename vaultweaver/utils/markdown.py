import re
HEADING_RX = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)

# --- snippet: safe_join ---
def safe_join(base: str, *parts: str) -> str:
    import os
    return os.path.normpath(os.path.join(base, *parts))
# --- endsnippet ---


# --- snippet: clamp_len ---
def clamp_len(s: str, n: int = 280) -> str:
    return s if len(s) <= n else s[:n-1] + "…"
# --- endsnippet ---

def extract_headings(md_text: str):
    return [(m.group(1), m.group(2).strip()) for m in HEADING_RX.finditer(md_text or "")]

# --- snippet: top_tags ---
def top_tags(index: dict, n: int = 10):
    from collections import Counter
    c = Counter()
    for meta in index.values():
        c.update(meta.get("tags", []))
    return c.most_common(n)
# --- endsnippet ---

