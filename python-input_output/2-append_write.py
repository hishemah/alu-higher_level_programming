#!/usr/bin/python3
"""Module that defines append_write, which appends a string to a file."""


def append_write(filename="", text=""):
    """Append text at the end of a UTF8 file, creating it if needed.

    Returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
