#!/usr/bin/python3
"""Export the TODO lists of all employees to a single JSON file.

Usage: ./3-dictionary_of_list_of_dictionaries.py

Creates todo_all_employees.json formatted as:
{"USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ...], ...}
"""
from collections import OrderedDict
import json
import requests

API_URL = "https://jsonplaceholder.typicode.com"


def export_all_to_json():
    """Write the tasks of every employee to todo_all_employees.json."""
    users = requests.get("{}/users".format(API_URL)).json()
    todos = requests.get("{}/todos".format(API_URL)).json()

    tasks_by_user = {}
    for task in todos:
        tasks_by_user.setdefault(task.get("userId"), []).append(task)

    all_tasks = OrderedDict()
    for user in users:
        user_id = user.get("id")
        all_tasks[str(user_id)] = [
            OrderedDict([("username", user.get("username")),
                         ("task", task.get("title")),
                         ("completed", task.get("completed"))])
            for task in tasks_by_user.get(user_id, [])]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_to_json()
