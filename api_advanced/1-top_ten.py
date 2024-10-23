#!/usr/bin/python3
"""Module that queries the Reddit API and prints top ten hot posts."""
import json
import requests
import sys


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {
        'User-Agent': 'linux:0.1.0 (by /u/your_username)'
    }
    params = {
        'limit': 10
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                              allow_redirects=False)
        if response.status_code == 404:
            print("None")
            return
        response_dict = response.json()
        posts = response_dict.get('data', {}).get('children', [])
        
        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get('data', {}).get('title'))

    except Exception:
        print("None")
        return