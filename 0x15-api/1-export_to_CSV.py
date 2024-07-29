#!/usr/bin/python3
"""
Script that uses the previous task to export to-do list
information for a given employee ID to CSV.
"""

import csv
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

    # Get to-do list items for relevanet user ID and convert to JSON object
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Use list comprehension to go ober to-do list items as a row in CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]
