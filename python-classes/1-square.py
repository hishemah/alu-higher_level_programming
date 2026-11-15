#!/usr/bin/python3
"""This module defines a class Square with a private size attribute."""


class Square:
    """A class that defines a square by its private size."""

    def __init__(self, size):
        """Initialize a new square with the given size.

        Args:
            size: The length of one side of the square.
        """
        self.__size = size
