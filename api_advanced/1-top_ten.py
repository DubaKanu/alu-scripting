#!/usr/bin/python3
"""Queries the Reddit API and prints top ten hot posts."""
import json
import requests
import sys


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0.1.0 (by /u/your_username)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {})
        children = data.get("children", [])

        if not children:
            print(None)
            return

        for child in children:
            print(child.get("data", {}).get("title", ""))

    except Exception:
        print(None)