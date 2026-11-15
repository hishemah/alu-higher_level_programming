#!/usr/bin/python3
"""Unittests for models/square.py."""
import io
import os
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Reset the automatic id counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove the file the tests may have written."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_is_rectangle(self):
        """A Square is a Rectangle and a Base."""
        s = Square(1)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_arguments(self):
        """Square(1), Square(1, 2), Square(1, 2, 3), Square(1, 2, 3, 4)."""
        s = Square(1)
        self.assertEqual((s.size, s.x, s.y, s.id), (1, 0, 0, 1))
        s = Square(1, 2)
        self.assertEqual((s.size, s.x, s.y, s.id), (1, 2, 0, 2))
        s = Square(1, 2, 3)
        self.assertEqual((s.size, s.x, s.y, s.id), (1, 2, 3, 3))
        s = Square(1, 2, 3, 4)
        self.assertEqual((s.size, s.x, s.y, s.id), (1, 2, 3, 4))

    def test_missing_size(self):
        """The size is required."""
        with self.assertRaises(TypeError):
            Square()

    def test_size_is_width_and_height(self):
        """The size is stored as the width and the height."""
        s = Square(5)
        self.assertEqual((s.width, s.height), (5, 5))
        s.size = 10
        self.assertEqual((s.size, s.width, s.height), (10, 10, 10))

    def test_types(self):
        """Every attribute must be an integer."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")
        s = Square(1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_values(self):
        """size must be > 0, x and y must be >= 0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_area(self):
        """area() returns size * size."""
        self.assertEqual(Square(5).area(), 25)

    def test_display(self):
        """display() prints the square, offset by x and y."""
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            Square(2, 2, 1).display()
        self.assertEqual(buffer.getvalue(), "\n  ##\n  ##\n")

    def test_str(self):
        """__str__ returns [Square] (<id>) <x>/<y> - <size>."""
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(2, 2)), "[Square] (2) 2/0 - 2")
        self.assertEqual(str(Square(3, 1, 3)), "[Square] (3) 1/3 - 3")

    def test_update_args(self):
        """update(1, 2, 3, 4) sets id, size, x and y."""
        s = Square(5)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """update(**{'id': 89, ...}) sets attributes by name."""
        s = Square(5)
        s.update(**{'id': 89})
        self.assertEqual(str(s), "[Square] (89) 0/0 - 5")
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(str(s), "[Square] (89) 2/0 - 1")
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (89) 2/1 - 7")

    def test_to_dictionary(self):
        """to_dictionary() returns id, x, size and y."""
        s = Square(10, 2, 1)
        self.assertEqual(s.to_dictionary(),
                         {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        s2 = Square(1, 1)
        s2.update(**s.to_dictionary())
        self.assertEqual(str(s2), str(s))
        self.assertIsNot(s, s2)

    def test_create(self):
        """Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_save_to_file(self):
        """Square.save_to_file(None), ([]) and ([Square(1)])."""
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([Square(1)])
        self.assertEqual(str(Square.load_from_file()[0]),
                         "[Square] (1) 0/0 - 1")

    def test_load_from_file_no_file(self):
        """Square.load_from_file() returns [] without a file."""
        self.assertEqual(Square.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
