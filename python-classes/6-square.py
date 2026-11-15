#!/usr/bin/python3
"""This module defines a class Square with a size and a position."""


class Square:
    """A class that defines a square printed at a given position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square with a size and a position.

        Args:
            size: The length of one side of the square.
            position: A tuple of 2 positive integers giving the offset
                used when printing the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position used when printing the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position used when printing the square after checking it.

        Args:
            value: A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character at its position.

        Prints an empty line if the size is 0. position[1] gives the number
        of empty lines printed first, and position[0] the number of spaces
        before each row.
        """
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
