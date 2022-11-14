#!/usr/bin/python3

"""
export json file to csv
"""
import csv
from os import sys
import requests


if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get("{}/users/{}".format(url, id)).json()
    todos = requests.get("{}/todos".format(url), params={"userId": id}).json()

    json_todo = {}
    todo_list = []
    for todo in todos:
        del todo["id"]
        todo["name"] = user.get("name")
        todo_list.append(todo)
    field_name = ["userId", "name", "completed", "title"]
    with open("USER_ID.csv", 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name)
        writer.writerows(todo_list)
