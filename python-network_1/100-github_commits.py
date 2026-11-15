#!/usr/bin/python3
"""List the 10 most recent commits of a GitHub repository.

Each line shows: <sha>: <author name>
Usage: ./100-github_commits.py <repository name> <owner name>
"""
import sys
import requests


if __name__ == "__main__":
    repo, owner = sys.argv[1], sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)
    for commit in response.json()[:10]:
        author = commit.get("commit").get("author").get("name")
        print("{}: {}".format(commit.get("sha"), author))
