#!/usr/bin/python3
"""
Module for number_of_subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns number of subscribers
    If not a valid subreddit, return 0.
    """
    data = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if data.status_code == 200:
        return data.json().get("data").get("subscribers")
    else:
        return 0
