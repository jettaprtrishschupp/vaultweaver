



# --- snippet: normalize_title ---
def normalize_title(title: str) -> str:
    return " ".join(title.strip().split())
# --- endsnippet ---


# --- snippet: safe_join ---
def safe_join(base: str, *parts: str) -> str:
    import os
    return os.path.normpath(os.path.join(base, *parts))
# --- endsnippet ---

