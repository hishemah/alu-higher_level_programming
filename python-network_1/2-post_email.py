#!/usr/bin/python3
"""Send a POST request with an email to a URL and display the response body.

Usage: ./2-post_email.py <URL> <email>
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode("utf-8"))
