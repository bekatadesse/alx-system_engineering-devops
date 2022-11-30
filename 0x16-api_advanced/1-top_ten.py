#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit.
"""
import requests


def top_ten(subreddit):
    """ this functiion returns the number of subscriber
    """
    endpoint = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "user one (by u/Known_Comb558)"}    
    params = {
        "limit": 10
    }
    response = requests.get(endpoint, headers=headers, params=params)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(r.get("data").get("title")) for r in results.get("children")]
