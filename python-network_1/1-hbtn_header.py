#!/usr/bin/python3
"""Send a request to a URL and display the value of its X-Request-Id header.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
