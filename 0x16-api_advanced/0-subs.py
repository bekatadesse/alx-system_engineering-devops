#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ this functiion returns the number of subscriber
    """
    endpoint = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "user one (by u/Known_Comb558)"}
    response = requests.get(endpoint, headers=headers)
    if response.status_code != 200:
        return 0
    return response.json()['data']['subscribers']
