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


