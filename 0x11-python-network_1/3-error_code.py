#!/usr/bin/python3
"""
Module: 3-error_code

Sends a request to a URL and displays the body of the response.
Handles urllib.error.HTTPError exceptions.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body_response = response.read().decode('utf-8')
            print(body_response)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
