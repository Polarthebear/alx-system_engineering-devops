#!/usr/bin/python3
"""
Program that returns a to-do list information for a given employee ID.

The .py script takes the employee ID as an argument from the CLI and
fetches the relevant user information and
the to-list from the JSONPlaceholder API,
the proceeds to print the task that the employee completed.
"""

import requests
import sys

if __name__ == "__main__":
    # URL for the placeholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Use employee ID to get the relevant employee info
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Use emplyee ID to gather the to-do list
    parameters = {"userId": employee_id}
    todos = requests.get(url + "todos", parameters).json()

    # Use filtering to count completed tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print employee name and completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the tasks completed with indents
    [print("\t {}".format(completed)) for complete in completed]
