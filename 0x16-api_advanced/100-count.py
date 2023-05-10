#!/usr/bin/python3
""" Advanced API """
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """ queries the Reddit API """
    if word_count == {}:
        word_count = {word.lower(): 0 for word in word_list}
    else:
        word_count = {k.lower(): v for k, v in word_count.items()}

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    if sub_info.status_code != 200:
        return None

    info = sub_info.json()

    hot_l = [child.get("data").get("title").lower()
             for child in info.get("data").get("children")]

    for title in hot_l:
        split_words = title.split()
        for word in word_list:
            if (word in split_words) and not any([
                split_word.startswith(word) and
                split_word[len(word):].isalnum()
                for split_word in split_words
            ]):
                word_count[word.lower()] += split_words.count(word)

    if not info.get("data").get("after"):
        sorted_counts = sorted(word_count.items(),
                               key=lambda kv: (-kv[1], kv[0]))
        for k, v in sorted_counts:
            if v > 0:
                print('{}: {}'.format(k, v))
    else:
        return count_words(subreddit, word_list, word_count,
                           info.get("data").get("after"))
