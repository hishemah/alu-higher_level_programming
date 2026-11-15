#!/usr/bin/python3
"""Send a POST request with an email to a URL and display the response body.

Usage: ./6-post_email.py <URL> <email>
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)
