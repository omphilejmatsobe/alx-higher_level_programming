#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository “rails”
by the user “rails”
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    list 10 commits (from the most recent to oldest) of the repository
    “rails” by the user “rails”
    """
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    req = requests.get(url)
    res_list = req.json()
    try:
        for x in range(10):
            print("{}: {}".format(res_list[x].get('sha'), res_list[x].
                                  get('commit').get('author').get('name')))
    except Exception:
        pass
