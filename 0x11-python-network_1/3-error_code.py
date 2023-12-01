#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """
    takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8)
    """
    u = argv[1]
    req = urllib.request.Request(u)
    try:
        with urllib.request.urlopen(req) as res:
            html = res.read()
            html_str = html.decode('utf-8')
            print(html_str)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
