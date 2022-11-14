#!/usr/bin/python3
"""
fetch a data from API
"""
from os import sys
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    id = sys.argv[1]
    todo_completed = requests.get('{}/todos'.format(url),
                                  params={"userId": id,
                                          "completed": "true"}).json()

    todo = requests.get('{}/todos?userId={}'.format(url, id)).json()
    user = requests.get('{}/users/{}'.format(url, id)).json()
    user_name = user.get('name')
    completed_total = len(todo_completed)
    total_todo = len(todo)
    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                          completed_total,
                                                          total_todo))
    for index in todo:
        if (index.get('completed') is True):
            print("\t {}".format(index.get('title')))
