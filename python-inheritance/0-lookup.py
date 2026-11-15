#!/usr/bin/python3
"""This module defines a function that lists the attributes of an object."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list with the names of the attributes and methods of obj.
    """
    return dir(obj)
