#!/usr/bin/python3
"""
Module: 7-error_code

Sends a request to a URL and displays the body of the response.
Prints an error code if the HTTP status code is >= 400.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
