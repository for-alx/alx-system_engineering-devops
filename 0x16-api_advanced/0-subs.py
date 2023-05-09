#!/usr/bin/python3
""" queries the Reddit API """


def number_of_subscribers(subreddit):
    """ Advanced API """
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(str(subreddit))
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'},
                     allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0
    return r.get('data').get('subscribers')
