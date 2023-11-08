#!/usr/bin/python3
"""extend Python script in task #0 to export data in the JSON format"""
import json
import requests

if __name__ == "__main__":

    api = "https://jsonplaceholder.typicode.com/"
    users = f"{api}users"
    users_data = {}

    users_json = json.loads(requests.get(users).text)

    for user in users_json:
        id = user.get('id')
        username = user.get('username')
        tasks = f"{api}users/{user.get('id')}/todos"
        tasks_json = json.loads(requests.get(tasks).text)

        users_data[id] = []
        for task in tasks_json:
            users_data[id].append({
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            })

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(users_data, f)
