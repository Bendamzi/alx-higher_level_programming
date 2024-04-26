#!/usr/bin/python3
"""
Module: 0-hbtn_status

Fetches https://alx-intranet.hbtn.io/status using urllib
and displays the body response.
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body_response = response.read()
        print("Body response:")
        print("\t- type:", type(body_response))
        print("\t- content:", body_response)
        print("\t- utf8 content:", body_response.decode('utf-8'))