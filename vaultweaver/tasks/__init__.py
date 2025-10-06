
# --- snippet: guess_language ---
def guess_language(text: str) -> str:
    import re
    cyr = len(re.findall(r"[А-Яа-яЁё]", text))
    lat = len(re.findall(r"[A-Za-z]", text))
    if cyr > lat: return "ru"
    if lat > cyr: return "en"
    return "unknown"
# --- endsnippet ---

