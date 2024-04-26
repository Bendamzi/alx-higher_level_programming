#!/usr/bin/python3
"""
Module: 10-my_github

Uses Basic Authentication with a personal access
token to access GitHub API and display user id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = f'https://api.github.com/users/{username}'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id)
    else:
        print(None)
