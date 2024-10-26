#!/usr/bin/python3
"""
This module contains the function top_ten.
"""
import requests
from sys import argv


def top_ten(subreddit):
    """
    Returns the top ten posts for a given subreddit.
    """
    user = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)

    try:
        response = requests.get(url, headers=user, allow_redirects=False)
        response.raise_for_status()
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
        print("OK")
    except requests.exceptions.RequestException:
        print("None")
    except ValueError:
        print("None")


if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Usage: ./script.py <subreddit>")