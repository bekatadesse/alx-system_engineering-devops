#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """ this functiion returns the number of subscriber
    <platform>:<app ID>:<version string> (by /u/<reddit username>)
    """
    endpoint = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "user one (by u/Known_Comb558)"
    }
    response = requests.get(endpoint, headers=headers)
    if response.status_code != 200:
        return 0
    return response.json()['data']['subscribers']