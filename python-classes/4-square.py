#!/usr/bin/python3
"""This module defines a class Square with a size property."""


class Square:
    """A class that defines a square whose size has a getter and a setter."""

    def __init__(self, size=0):
        """Initialize a new square with the given size.

        Args:
            size: The length of one side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the length of one side of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the length of one side of the square after checking it.

        Args:
            value: The new length of one side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
