
# autosave 2025-10-03T11:41:09.984145

# --- snippet: normalize_title ---
def normalize_title(title: str) -> str:
    return " ".join(title.strip().split())
# --- endsnippet ---


# --- snippet: clamp_len ---
def clamp_len(s: str, n: int = 280) -> str:
    return s if len(s) <= n else s[:n-1] + "…"
# --- endsnippet ---

