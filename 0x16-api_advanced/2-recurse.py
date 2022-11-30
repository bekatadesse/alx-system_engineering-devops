#!/usr/bin/python3
""" Function to query subscribers on a given Reddit subreddit """
import requests

def recurse(subreddit, hotlist=[], after=None):
    """ this functiion returns the number of subscriber """
    head = {'User-Agent': "user one (by u/Known_Comb558)"}
    try:
        if after:
            count = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after), headers=head).json().get('data')
        else:
            count = requests.get('https://www/reddit.com/r/{}/hot.json'.format(
                subreddit), headers=head).json().get('data')
        hotlist += [dic.get('data').get('title')
                    for dic in count.get('children')]
        if count.get('after'):
            return recurse(subreddit, hotlist, after=count.get('after'))
        return hotlist
    except:
        return None
