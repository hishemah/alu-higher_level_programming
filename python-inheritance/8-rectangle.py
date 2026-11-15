#!/usr/bin/python3
"""This module defines a class Rectangle based on BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a private width and height."""

    def __init__(self, width, height):
        """Initialize a new rectangle after validating its sides.

        Args:
            width: The width of the rectangle, a positive integer.
            height: The height of the rectangle, a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
