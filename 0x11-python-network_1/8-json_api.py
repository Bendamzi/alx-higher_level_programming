#!/usr/bin/python3
"""
Module: 8-json_api

Sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.
Processes the response and displays the id and name if
JSON is valid and not empty.
"""

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    data = {'q': q}
    response = requests.post(url, data=data)

    try:
        result = response.json()
        if result:
            print(f"[{result['id']}] {result['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
