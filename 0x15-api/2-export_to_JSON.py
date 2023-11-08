#!/usr/bin/python3
"""extend Python script in task #0 to export data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":

    id = sys.argv[1]
    api = "https://jsonplaceholder.typicode.com/"
    user = f"{api}users/{id}"
    user_tasks = f"{user}/todos"
    user_data = {id: []}

    username = json.loads(requests.get(user).text).get('username')
    user_tasks_json = json.loads(requests.get(user_tasks).text)

    for task in user_tasks_json:
        user_data[id].append({"task": task.get('title'),
                              "completed": task.get('completed'),
                              "username": username})

    with open(f"{id}.json", "w", encoding="utf-8") as f:
        json.dump(user_data, f)
