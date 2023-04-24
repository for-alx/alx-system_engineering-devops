#!/usr/bin/python3
""" Export to CSV  """
import requests
import sys

if __name__ == "__main__":
    argument = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(argument)).json()
    todo = requests.get(url + 'todos?userId={}'.format(argument)).json()
    user_status = '"{}","{}",'.format(user.get('id'), user.get('username'))
    csv_file_name = '{}.csv'.format(user.get('id'))

    with open(csv_file_name, 'a') as f:
        for task in todo:
            task_status = '"{}","{}"'.format(
                task.get('completed'), task.get('title'))
            f.write(user_status + task_status + '\n')
