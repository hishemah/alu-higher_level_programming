#!/usr/bin/python3
"""Module that defines class_to_json for JSON serialization of objects."""


def class_to_json(obj):
    """Return the dictionary description of an object's attributes.

    The values are simple data structures (list, dictionary, string,
    integer and boolean), ready for JSON serialization.
    """
    return obj.__dict__
