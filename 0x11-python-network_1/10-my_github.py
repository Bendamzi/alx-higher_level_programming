#!/usr/bin/python3
"""
Module: 10-my_github

Uses Basic Authentication with a personal
access token to access GitHub API and display user id.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    if len(sys.argv) > 2:
        username = sys.argv[1]
        token = sys.argv[2]
        auth = HTTPBasicAuth(username, token)
        url = "https://api.github.com/user"
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            user_data = response.json()
            print(user_data.get("id"))
        else:
            print("None")
