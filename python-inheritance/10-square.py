#!/usr/bin/python3
"""This module defines a class Square based on Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square, which is a rectangle with equal sides."""

    def __init__(self, size):
        """Initialize a new square after validating its size.

        Args:
            size: The length of the sides of the square, a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
