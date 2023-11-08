#!/usr/bin/python3
"""extend Python script in task #0 to export data in the CSV format"""
import csv
import json
import requests
import sys

if __name__ == "__main__":

    id = sys.argv[1]
    user_tasks = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    user = f"https://jsonplaceholder.typicode.com/users/{id}/"
    user_tasks_csv = []

    user_tasks_json = json.loads(requests.get(user_tasks).text)
    username = json.loads(requests.get(user).text).get('username')
    user_id = json.loads(requests.get(user).text).get('id')

    for task in user_tasks_json:
        user_tasks_csv.append([user_id, username,
                               task.get('completed'), task.get('title')])

    with open(f"{id}.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=1)

        for task in user_tasks_csv:
            writer.writerow(task)
