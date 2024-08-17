#!/usr/bin/python3
"""Function that queries Reddit API & returns the number of subscribers."""

import requests

#!/usr/bin/python3
"""Function that queries Reddit API & returns the number of subscribers."""

import requests


def number_of_subscribers(subreddit):
    """Return total subreddit subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Polarbear325"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
