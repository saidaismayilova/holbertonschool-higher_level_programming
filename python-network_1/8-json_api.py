#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    # If no argument is provided, q = ""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        response = requests.post(url, data=payload)
        # Try to parse JSON
        try:
            data = response.json()
        except ValueError:
            print("Not a valid JSON")
            sys.exit(0)

        # Check if empty JSON
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))

    except Exception as e:
        print("Not a valid JSON")
