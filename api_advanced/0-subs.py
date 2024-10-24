#!/usr/bin/python3
"""This module contains functions to interact with the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """Query the Reddit API and return the number of subscribers for a given subreddit."""
    # Reddit API URL
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom headers to avoid Too Many Requests error
    headers = {
        'User-Agent': 'linux:0.1.0 (by /u/your_username)'
    }

    try:
        # Make GET request to Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0

    except Exception:
        return 0