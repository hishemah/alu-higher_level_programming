#!/usr/bin/python3
"""This module defines a function that checks if an object is a subclass
instance of a given class.
"""


def inherits_from(obj, a_class):
    """Check whether an object is an instance of a strict subclass of a class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is an instance of a class derived (directly or
        indirectly) of a_class but not of a_class itself, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
