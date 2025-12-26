import requests

BASE_URL = "https://codeforces.com/api"


def get_user_info(handle: str):
    """
    Fetch basic user information from Codeforces.
    """
    url = f"{BASE_URL}/user.info"
    params = {"handles": handle}

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] != "OK":
        raise Exception("Failed to fetch user info")

    return data["result"][0]


def get_user_submissions(handle: str, limit: int = 1000):
    """
    Fetch recent submissions of a user.
    """
    url = f"{BASE_URL}/user.status"
    params = {
        "handle": handle,
        "count": limit
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] != "OK":
        raise Exception("Failed to fetch submissions")

    return data["result"]

if __name__ == "__main__":
    subs = get_user_submissions("aditisahu12", 50)
    print(subs[0]["problem"]["tags"])
