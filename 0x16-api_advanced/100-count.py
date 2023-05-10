#!/usr/bin/python3
""" Advanced API """
import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    """ queries the Reddit API """
    sub_info = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                            .format(subreddit, after),
                            headers={"User-Agent": "My-User-Agent"})
    if after is None:
        word_list = [word.lower() for word in word_list]

    if sub_info.status_code == 200:
        sub_info = sub_info.json()['data']
        aft = sub_info['after']
        sub_info = sub_info['children']
        for post in sub_info:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
