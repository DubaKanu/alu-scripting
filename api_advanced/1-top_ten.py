#!/usr/bin/python3
"""
Reddit API top posts retrieval module.

This module provides functionality for retrieving hot posts from Reddit
using the Reddit API.
"""
import requests


def top_ten(subreddit):
    """Function that queries Reddit API and prints first 10 hot posts titles."""
    # Reddit API URL for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Custom headers to avoid Too Many Requests error
    headers = {
        'User-Agent': 'linux:0.1.0 (by /u/your_username)'
    }

    # Parameters to limit the number of posts and get required fields
    params = {
        'limit': 10
    }

    try:
        # Make GET request to Reddit API
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            # Print the title of each post
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)

    except Exception:
        print(None)