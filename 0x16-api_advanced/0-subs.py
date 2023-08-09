#!/usr/bin/python3
"""
A python script that gets the number of subscribers from a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    A function that make execution to get the request
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url,
                            allow_redirects=False,
                            headers={'User-Agent': 'MyChromeBook'})
    if response:
        suscribers_number = response.json().get('data').get('subscribers')
        return suscribers_number
    else:
        return 0
