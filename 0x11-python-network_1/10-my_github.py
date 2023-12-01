#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes your Github credentials (username and password) and uses the
    Github API to display your id
    """
    usr = argv[1]
    passwrd = argv[2]
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(usr, passwrd))
    try:
        print(req.json().get('id'))
    except Exception:
        pass
