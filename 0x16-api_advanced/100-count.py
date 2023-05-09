#!/usr/bin/python3
""" Advanced API """
import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """ queries the Reddit API """
    if not word_count:
        word_count = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return

    data = response.json()["data"]
    after = data["after"]
    articles = data["children"]

    for article in articles:
        title = article["data"]["title"].lower()
        for word in word_list:
            if (f" {word.lower()} " in f" {title} " or
                    title.startswith(f"{word.lower()} ") or
                    title.endswith(f" {word.lower()}") or
                    title == f"{word.lower()}"):
                if word.lower() in word_count:
                    word_count[word.lower()] += 1
                else:
                    word_count[word.lower()] = 1

    if not after:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
    else:
        count_words(subreddit, word_list, word_count, after)
