#!/usr/bin/python3
"""
Script that uses GitHub API to display the authenticated user's id.
"""

import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]  # personal access token

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    try:
        data = response.json()
        print(data.get("id"))
    except Exception:
        print("None")
