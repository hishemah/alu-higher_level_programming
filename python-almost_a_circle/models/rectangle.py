#!/usr/bin/python3
"""Module that defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle, with a position (x, y)."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
            x (int): the horizontal offset of the rectangle.
            y (int): the vertical offset of the rectangle.
            id (int): the id of the rectangle.

        Raises:
            TypeError: if width, height, x or y is not an integer.
            ValueError: if width or height is <= 0, or x or y is < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def _validate(name, value, minimum):
        """Check that value is an integer and at least minimum.

        Args:
            name (str): the attribute name used in error messages.
            value: the value to check.
            minimum (int): 1 for width and height, 0 for x and y.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < minimum:
            if minimum > 0:
                raise ValueError("{} must be > 0".format(name))
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """int: the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self._validate("width", value, 1)
        self.__width = value

    @property
    def height(self):
        """int: the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self._validate("height", value, 1)
        self.__height = value

    @property
    def x(self):
        """int: the horizontal offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self._validate("x", value, 0)
        self.__x = value

    @property
    def y(self):
        """int: the vertical offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self._validate("y", value, 0)
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the character #, offset by x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle.

        Args:
            *args: new values, in this order: id, width, height, x, y.
            **kwargs: new values by attribute name, used only when no
                positional argument is given.
        """
        names = ("id", "width", "height", "x", "y")
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in names:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
