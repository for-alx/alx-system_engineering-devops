#!/usr/bin/python3
""" Gather data from an API """
import requests
import sys

argument = sys.argv[1]
url = 'https://jsonplaceholder.typicode.com/'
user = requests.get(url + 'users/{}'.format(argument)).json()
todo = requests.get(url + 'todos?userId={}'.format(argument)).json()
total_completed = 0

for task in todo:
    if task.get('completed') is True:
        total_completed += 1

print('Employee {} is done with tasks({}/{}):'.format(
    user.get('name'), total_completed, len(todo)))

for task in todo:
    if task.get('completed') is True:
        print('\t', task.get('title'))
