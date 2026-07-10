import requests

BASE = "https://codeforces.com/api"

def get_submissions(handle, limit=10000):
    r = requests.get(f"{BASE}/user.status", params={"handle": handle, "count": limit})
    r.raise_for_status()
    data = r.json()
    if data["status"] != "OK":
        raise ValueError(data.get("comment", "Codeforces API error"))
    return data["result"]

get_user_submissions = get_submissions

# Backward-compatible alias in case other files still import the old name
get_user_submissions = get_submissions

def get_user_info(handle):
    r = requests.get(f"{BASE}/user.info", params={"handles": handle})
    r.raise_for_status()
    data = r.json()
    if data["status"] != "OK":
        raise ValueError(data.get("comment", "Codeforces API error"))
    return data["result"][0]

def get_rating_history(handle):
    r = requests.get(f"{BASE}/user.rating", params={"handle": handle})
    r.raise_for_status()
    data = r.json()
    if data["status"] != "OK":
        raise ValueError(data.get("comment", "Codeforces API error"))
    return data["result"]

def get_problemset(tags=None, max_rating=None, min_rating=None):
    params = {}
    if tags:
        params["tags"] = ";".join(tags)
    r = requests.get(f"{BASE}/problemset.problems", params=params)
    r.raise_for_status()
    data = r.json()
    if data["status"] != "OK":
        raise ValueError(data.get("comment", "Codeforces API error"))
    problems = data["result"]["problems"]
    if min_rating:
        problems = [p for p in problems if p.get("rating", 0) >= min_rating]
    if max_rating:
        problems = [p for p in problems if p.get("rating", 0) <= max_rating]
    return problems