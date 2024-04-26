#!/usr/bin/python3
"""
Module: 100-github_commits

Lists 10 commits (from most recent to oldest) of a
specified repository by a given user using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repository}/commits'

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:  # Get the 10 most recent commits
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error fetching commits:", response.status_code)
