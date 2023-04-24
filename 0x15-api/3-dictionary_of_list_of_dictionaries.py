#!/usr/bin/python3
""" Dictionary of list of dictionaries """
import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    json_file_name = 'todo_all_employees.json'
    dictionary = {}

    for i in range(1, 11):
        user = requests.get(url + 'users/{}'.format(i)).json()
        todo = requests.get(url + 'todos?userId={}'.format(i)).json()
        id = user.get('id')
        singl_user = []
        for task in todo:
            dic = {
                'username': user.get('username'),
                'task': task.get('title'),
                'completed': task.get('completed')
            }
            singl_user.append(dic)

        dictionary[id] = singl_user

    with open(json_file_name, 'w') as f:
        json.dump(dictionary, f)
