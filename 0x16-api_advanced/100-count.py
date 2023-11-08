#!/usr/bin/python3
"""recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces)"""
import requests


def count_words(subreddit, word_list, words={}, after=None):
    if words == {}:
        for word in word_list:
            words[word] = 0

    api = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    res = requests.get(api, headers={
        "User-Agent": "Mozilla/5.0"
    }, allow_redirects=False)

    if res.status_code != 200:
        pass
    else:
        data = res.json().get("data")
        after = data.get("after")

        for post in data.get("children"):
            for title in post.get("data").get("title").split():
                if title.lower() in word_list:
                    words[title.lower()] += 1

        if not after:
            sorted_word_list = sorted(words)
            for word in sorted_word_list:
                if words[word] != 0:
                    print(f"{word}: {words[word]}")
        return count_words(subreddit, word_list, words, after)
