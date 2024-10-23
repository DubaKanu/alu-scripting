#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
  """
  This function queries the Reddit API to get the number of subscribers for a given subreddit.

  Args:
      subreddit: The name of the subreddit to query (string).

  Returns:
      The number of subscribers for the subreddit (integer), or 0 if the subreddit is invalid.
  """

  # Build the API endpoint URL
  url = f"https://www.reddit.com/r/{subreddit}/about.json?limit=0"

  # Set a custom User-Agent header to avoid "Too Many Requests" errors
  headers = {"User-Agent": "MyCoolScript/1.0"}

  # Send a GET request without following redirects
  response = requests.get(url, allow_redirects=False, headers=headers)

  # Check for successful response (200 OK)
  if response.status_code == 200:
    data = response.json()
    # Extract the subscriber count from the data
    return data.get("data", {}).get("subscribers", 0)
  else:
    # Invalid subreddit or other error
    return 0

# Example usage
subreddit_name = "learnpython"
number_of_subs = number_of_subscribers(subreddit_name)

if number_of_subs > 0:
  print(f"The subreddit '{subreddit_name}' has {number_of_subs} subscribers.")
else:
  print(f"The subreddit '{subreddit_name}' is invalid or could not be found.")