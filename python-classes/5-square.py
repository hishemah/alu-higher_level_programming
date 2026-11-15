#!/usr/bin/python3
"""This module defines a class Square that can print itself with #."""


class Square:
    """A class that defines a square that can be printed to stdout."""

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

    def my_print(self):
        """Print the square with the # character, or an empty line if 0."""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)
