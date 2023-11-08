#!/usr/bin/python3
"""Python script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress"""
import json
import requests
import sys


if __name__ == "__main__":

    id = sys.argv[1]
    api = "https://jsonplaceholder.typicode.com/"
    user_data = f"{api}users/{id}"
    user_tasks = f"{api}users/{id}/todos"
    done_tasks = f"{api}users/{id}/todos?completed=true"

    user_json = json.loads(requests.get(user_data).text)
    tasks_json = json.loads(requests.get(user_tasks).text)
    done_tasks_json = json.loads(requests.get(done_tasks).text)

    no_tasks = len(tasks_json)
    no_done_tasks = len(done_tasks_json)

    print(f"Employee {user_json.get('name')} is done with tasks"
          f"({no_done_tasks}/{no_tasks}):")

    for task in done_tasks_json:
        print(f"\t {task.get('title')}")
