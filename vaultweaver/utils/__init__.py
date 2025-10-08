
# --- snippet: clamp_len ---
def clamp_len(s: str, n: int = 280) -> str:
    return s if len(s) <= n else s[:n-1] + "…"
# --- endsnippet ---

