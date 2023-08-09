#!/usr/bin/python3
"""
A python script that Request the top ten hot posts
"""
import requests


def top_ten(subreddit):
    """
    A function that gets the top ten hot post of a subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url,
                            allow_redirects=False,
                            headers={'User-Agent': 'Pear'})
    if response:
        post_list = response.json().get('data').get('children')
        for i, children in enumerate(post_list):
            if (i == 10):
                break
            print(children.get('data').get('title'))
    else:
        print(None)
