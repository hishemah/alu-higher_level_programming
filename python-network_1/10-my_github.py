#!/usr/bin/python3
"""Display your GitHub user id, using the GitHub API with Basic Authentication.

Usage: ./10-my_github.py <username> <personal access token>
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=(sys.argv[1], sys.argv[2]))
    print(response.json().get("id"))
