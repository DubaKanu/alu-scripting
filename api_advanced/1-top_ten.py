#!/usr/bin/python3
"""
This module contains functions to interact with the Reddit API.

It provides functionality to retrieve and print titles of hot posts
from a specified subreddit using Reddit's public API endpoints.

Functions:
    top_ten(subreddit): Prints titles of the first 10 hot posts
    for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
                        Do not include the /r/ prefix.

    Returns:
        None: This function prints the titles and doesn't return anything.
              Prints None if the subreddit is invalid or an error occurs.

    Example:
        >>> top_ten("python")
        [Prints first 10 hot post titles from r/python]
        >>> top_ten("this_subreddit_does_not_exist")
        None
    """
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