#!/usr/bin/python3
"""Send a request to a URL and display the value of its X-Request-Id header.

Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
