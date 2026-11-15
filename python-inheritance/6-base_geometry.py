#!/usr/bin/python3
"""This module defines a class BaseGeometry with an area method."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Compute the area of the shape, which is not implemented here.

        Raises:
            Exception: Always, because the base class has no area.
        """
        raise Exception("area() is not implemented")
