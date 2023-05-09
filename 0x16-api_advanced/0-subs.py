#!/usr/bin/python3
""" queries the Reddit API """
import requests
import json


def number_of_subscribers(subreddit):
    """ """
    url = 'https://www.reddit.com/r/{}/about.json'.format(str(subreddit))
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).json()
    if sub_info.status_code >= 300:
        return 0
    return str(r.get('data').get('subscribers'))
