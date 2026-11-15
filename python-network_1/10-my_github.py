#!/usr/bin/python3
"""Display your GitHub user id, using the GitHub API with Basic Authentication.

Usage: ./10-my_github.py <username> <personal access token>
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
