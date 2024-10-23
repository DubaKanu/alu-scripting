#!/usr/bin/python3
"""Queries the Reddit API and prints top ten hot posts."""
import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0.1.0 (by /u/your_username)"
    }
    params = {
        "limit": 10
    }
    try:
        r = requests.get(url, headers=headers,
                        params=params, allow_redirects=False)
        if r.status_code != 200:
            print(None)
        else:
            data = r.json().get("data", {})
            children = data.get("children", [])
            if not children:
                print(None)
            for post in children:
                print(post.get("data", {}).get("title", ""))
    except Exception:
        print(None)