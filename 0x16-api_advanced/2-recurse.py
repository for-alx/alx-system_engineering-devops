#!/usr/bin/python3
"""Module for Reddit API"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Fetch all the hot posts from a subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"count": count, "after": after}
    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)

    if response.status_code >= 400:
        return None

    posts = [child.get("data").get("title")
             for child in response.json().get("data").get("children")]

    info = response.json()
    if not info.get("data").get("after"):
        return hot_list + posts

    return recurse(subreddit, hot_list + posts,
                   info.get("data").get("count"),
                   info.get("data").get("after"))
