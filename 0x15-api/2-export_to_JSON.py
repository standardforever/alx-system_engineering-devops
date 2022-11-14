#!/usr/bin/python3
"""
export to json
"""

import json
from os import sys
import requests


if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get("{}/users/{}".format(url, id)).json()
    todos = requests.get("{}/todos".format(url), params={"userId": id}).json()

    todo_dict = {}
    todo_list = []
    for todo in todos:
        todo_dict["task"] = todo["title"]
        todo_dict["completed"] = todo["completed"]
        todo_dict["username"] = user["username"]
        todo_list.append(todo_dict)
    new_dict = {}
    new_dict[id] = todo_list
    json_file = json.dumps(new_dict)
    with open("{}.json".format(id), "w") as r:
        r.write(json_file)
