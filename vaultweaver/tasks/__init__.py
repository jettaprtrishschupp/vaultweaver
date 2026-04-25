



# --- snippet: backlinks_map ---

# --- snippet: guess_language ---
def guess_language(text: str) -> str:
    import re
    cyr = len(re.findall(r"[А-Яа-яЁё]", text))
    lat = len(re.findall(r"[A-Za-z]", text))
    if cyr > lat: return "ru"
    if lat > cyr: return "en"
    return "unknown"
# --- endsnippet ---

def backlinks_map(index: dict) -> dict:
    back = {k: [] for k in index.keys()}
    # оставлено для апдейтера — можно доработать вставкой логики
    return back
# --- endsnippet ---

