#!/usr/bin/python3
"""
A python script that make a recursive call to query the redit API
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    A function that gets the top ten hot post of a subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    payload = {'after': after}
    response = requests.get(url,
                            allow_redirects=False,
                            params=payload,
                            headers={'User-Agent': 'Pear'})
    if response and response.status_code == 200:
        after = response.json().get('data').get('after')
        if (after is None):
            return hot_list
        post_list = response.json().get('data').get('children')
        for children in post_list:
            hot_list.append(children.get('data').get('title'))
        return recurse(subreddit, hot_list, after)
    else:
        return None
