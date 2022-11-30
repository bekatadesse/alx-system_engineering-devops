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
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(endpoint, headers=headers, params=params)
    if response.status_code != 200:
        return 0
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
