#!/usr/bin/python3
"""recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    api = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    res = requests.get(api, headers={
        "User-Agent": "Mozilla/5.0"
    }, allow_redirects=False)

    if res.status_code != 200:
        return None
    else:
        data = res.json().get("data")
        after = data.get("after")

        for post in data.get("children"):
            hot_list.append(post.get("data").get("title"))

        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)
