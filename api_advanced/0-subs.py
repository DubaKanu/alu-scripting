#!/usr/bin/python3
"""
This module contains functions to interact with the Reddit API.

It provides functionality to retrieve subscriber counts for subreddits
using Reddit's public API endpoints.

Functions:
    number_of_subscribers(subreddit): Returns the number of subscribers
    for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
                        Do not include the /r/ prefix.

    Returns:
        int: The number of subscribers if the subreddit exists and is valid.
             Returns 0 if the subreddit does not exist or an error occurs.

    Example:
        >>> number_of_subscribers("python")
        999999
        >>> number_of_subscribers("this_subreddit_does_not_exist")
        0
    """
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