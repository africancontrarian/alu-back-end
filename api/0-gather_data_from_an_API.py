!/usr/bin/python3
"""Gather an employee's TODO list progress from a REST API.
 
Usage: ./0-gather_data_from_an_API.py EMPLOYEE_ID
"""
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com"
 
 
def display_todo_progress(employee_id):
    """Print the TODO list progress of the employee with the given ID."""
    user = requests.get("{}/users/{}".format(API_URL, employee_id)).json()
    todos = requests.get("{}/todos".format(API_URL),
                         params={"userId": employee_id}).json()
 
    done_tasks = [task for task in todos if task.get("completed")]
 
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), len(todos)))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
 
 
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        display_todo_progress(int(sys.argv[1]))