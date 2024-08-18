#!/usr/bin/python3
"""Function that queries Reddit API & returns the number of subscribers."""

import requests


def number_of_subscribers(subreddit):
    """Return total subreddit subscribers."""
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Polarbear325'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    data = response.json().get('data')
    subs_number = data.get('subscribers')

    return subs_number
