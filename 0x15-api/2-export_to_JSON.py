#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Use employee ID to get the relevant employee info
    user_id = sys.argv[1]

    # URL for the placeholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get user infor and convert to JSON object
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Get user name from the data
    username = user.get("username")

    # Use emplyee ID to gather the to-do list
    parameters = {"userId": user_id}
    todos = requests.get(url + "todos", parameters).json()

    # Make dictionary with user and to-do list information
    data_to_export = {
            user_id: [
                {
                    "task": t.get("completed"),
                    "username": username
                }
                for t in todos
            ]
        }
    # Write relevant data to JSON file with employee_id as filename
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
