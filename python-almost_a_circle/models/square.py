#!/usr/bin/python3
"""Module that defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square, a rectangle whose width and height are equal."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): the length of a side of the square.
            x (int): the horizontal offset of the square.
            y (int): the vertical offset of the square.
            id (int): the id of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: the length of a side, stored as the width and height."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the attributes of the square.

        Args:
            *args: new values, in this order: id, size, x, y.
            **kwargs: new values by attribute name, used only when no
                positional argument is given.
        """
        names = ("id", "size", "x", "y")
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in names:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
