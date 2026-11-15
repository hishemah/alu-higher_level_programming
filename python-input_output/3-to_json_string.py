#!/usr/bin/python3
"""Module that defines to_json_string, a JSON serialization helper."""
import json


def to_json_string(my_obj):
    """Return the JSON representation (a string) of an object."""
    return json.dumps(my_obj)
