#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file.

Usage: ./2-export_to_JSON.py EMPLOYEE_ID

Creates USER_ID.json formatted as:
{"USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ...]}
"""
from collections import OrderedDict
import json
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com"


def export_to_json(employee_id):
    """Write every task owned by the given employee to USER_ID.json."""
    user = requests.get("{}/users/{}".format(API_URL, employee_id)).json()
    todos = requests.get("{}/todos".format(API_URL),
                         params={"userId": employee_id}).json()

    tasks = [OrderedDict([("task", task.get("title")),
                          ("completed", task.get("completed")),
                          ("username", user.get("username"))])
             for task in todos]

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        export_to_json(int(sys.argv[1]))
