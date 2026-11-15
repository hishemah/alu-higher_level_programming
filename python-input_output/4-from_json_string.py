#!/usr/bin/python3
"""Module that defines from_json_string, a JSON deserialization helper."""
import json


def from_json_string(my_str):
    """Return the Python data structure represented by a JSON string."""
    return json.loads(my_str)
