#!/usr/bin/python3
""" Export to JSON """
import json
import requests
import sys

if __name__ == "__main__":
    argument = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(argument)).json()
    todo = requests.get(url + 'todos?userId={}'.format(argument)).json()
    json_file_name = '{}.json'.format(user.get('id'))
    id = user.get('id')
    dictionary = {id: []}

    for task in todo:
        dic = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user.get('username')
        }
        dictionary.get(id).append(dic)

    with open(json_file_name, 'w') as f:
        json.dump(dictionary, f)
