#!/usr/bin/python3

"""
This module provides functions for querying the Reddit API to retrieve information about subreddits and posts.

Currently, it includes the following functionalities:

  * `top_ten(subreddit)`: This function queries the Reddit API to get the titles of the top 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
  """
  This function queries the Reddit API to get the titles of the top 10 hot posts for a given subreddit.

  Args:
      subreddit: The name of the subreddit to query (string).

  Returns:
      The titles of the top 10 hot posts as a list of strings, or None if the subreddit is invalid.
  """

  # Build the API endpoint URL
  url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

  # Set a custom User-Agent header to avoid "Too Many Requests" errors
  headers = {"User-Agent": "MyCoolScript/1.0"}

  # Send a GET request without following redirects
  response = requests.get(url, allow_redirects=False, headers=headers)

  # Check for successful response (200 OK)
  if response.status_code == 200:
    data = response.json()
    # Extract the post titles from the data
    posts = data.get("data", {}).get("children", [])
    titles = [post.get("data", {}).get("title") for post in posts]
    return titles
  else:
    # Invalid subreddit or other error
    return None

# Example usage
subreddit_name = "learnpython"
top_posts = top_ten(subreddit_name)

if top_posts:
  for title in top_posts:
    print(title)
else:
  print(f"The subreddit '{subreddit_name}' is invalid or could not be found.")