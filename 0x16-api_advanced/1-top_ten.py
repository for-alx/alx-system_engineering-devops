#!/usr/bin/python3
""" Advanced API """
import requests


def top_ten(subreddit):
    """ queries the Reddit API """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'},
                     allow_redirects=False)
    if r.status_code >= 300:
        print('None')
    else:
        # print(r.json().get('data').get('children'))
        # [print(child.get("data").get("title"))
        #  for child in r.json().get("data").get("children")]
        for title in r.json().get('data').get('children'):
            print(title.get('data').get('title'))
