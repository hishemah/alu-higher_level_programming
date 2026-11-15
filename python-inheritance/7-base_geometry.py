#!/usr/bin/python3
"""This module defines a class BaseGeometry that can validate integers."""


class BaseGeometry:
    """A base class for geometry shapes with an integer validator."""

    def area(self):
        """Compute the area of the shape, which is not implemented here.

        Raises:
            Exception: Always, because the base class has no area.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check that a value is a positive integer.

        Args:
            name: The name of the value, used in the error messages.
            value: The value to check.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
