#!/usr/bin/python3
"""Sends a POST request to a given URL with an email parameter"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare data
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    # Send POST request
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read()
        print(body.decode("utf-8"))
