#!/usr/bin/python3
"""Search a user by the letter given as argument with a POST request.

The request goes to http://0.0.0.0:5000/search_user with the variable q
(an empty string when no letter is given).
Usage: ./8-json_api.py [letter]
"""
import sys
import requests


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post("http://0.0.0.0:5000/search_user",
                             data={"q": letter})
    try:
        user = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if user:
            print("[{}] {}".format(user.get("id"), user.get("name")))
        else:
            print("No result")
