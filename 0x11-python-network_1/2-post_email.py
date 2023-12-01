#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter"""

import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
