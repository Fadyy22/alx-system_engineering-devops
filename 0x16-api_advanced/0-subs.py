#!/usr/bin/python3
"""function that queries the Reddit API
and returns the number of subscribers for a given subreddit"""
import json
import requests


def number_of_subscribers(subreddit):
    api = f"https://www.reddit.com/r/{subreddit}/about.json"
    data = json.loads(requests.get(f"{api}", headers={
        "User-Agent": "Mozilla/5.0"
    }).text)

    if data.get("error") == 404:
        return 0
    else:
        return data.get("data").get("subscribers")
