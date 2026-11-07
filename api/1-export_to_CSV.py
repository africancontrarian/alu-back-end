#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file.

Usage: ./1-export_to_CSV.py EMPLOYEE_ID

Creates USER_ID.csv with one row per task, formatted as:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""
import csv
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com"


def export_to_csv(employee_id):
    """Write every task owned by the given employee to USER_ID.csv."""
    user = requests.get("{}/users/{}".format(API_URL, employee_id)).json()
    todos = requests.get("{}/todos".format(API_URL),
                         params={"userId": employee_id}).json()

    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, user.get("username"),
                             task.get("completed"), task.get("title")])


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        export_to_csv(int(sys.argv[1]))
