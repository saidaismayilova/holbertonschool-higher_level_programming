#!/usr/bin/python3
"""
Script that sends a POST request to http://0.0.0.0:5000/search_user
with a letter as parameter.
"""

import sys
import requests


if __name__ == "__main__":
    # If no argument given → q = ""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        response = requests.post(url, data=payload)
        try:
            data = response.json()
        except ValueError:
            print("Not a valid JSON")
            sys.exit(0)

        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))

    except Exception:
        print("Not a valid JSON")
