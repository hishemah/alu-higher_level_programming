#!/usr/bin/python3
"""Unittests for models/rectangle.py."""
import io
import os
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Reset the automatic id counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove the file the tests may have written."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    @staticmethod
    def output(function):
        """Return what function() prints."""
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            function()
        return buffer.getvalue()

    def test_is_base(self):
        """A Rectangle is a Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_two_arguments(self):
        """Rectangle(1, 2) sets width and height, and an automatic id."""
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id), (1, 2, 0, 0, 1))
        self.assertEqual(Rectangle(10, 2).id, 2)

    def test_all_arguments(self):
        """Rectangle(1, 2, 3, 4, 5) sets every attribute."""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.x, r.y), (3, 4))
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id), (1, 2, 3, 4, 5))

    def test_missing_arguments(self):
        """Width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_private_attributes(self):
        """The attributes are private."""
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__width
        self.assertEqual(r._Rectangle__width, 1)

    def test_types(self):
        """Every attribute must be an integer."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.5, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_values(self):
        """width and height must be > 0, x and y must be >= 0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_validation_order(self):
        """width is checked first, then height, x and y."""
        with self.assertRaisesRegex(TypeError, "width"):
            Rectangle("1", "2", "3", "4")
        with self.assertRaisesRegex(ValueError, "height"):
            Rectangle(1, 0, -1, -1)

    def test_setters(self):
        """The setters validate new values too."""
        r = Rectangle(1, 2)
        r.width = 10
        r.height = 20
        r.x = 3
        r.y = 0
        self.assertEqual(str(r), "[Rectangle] (1) 3/0 - 10/20")
        with self.assertRaises(TypeError):
            r.width = "10"
        with self.assertRaises(ValueError):
            r.x = -1

    def test_area(self):
        """area() returns width * height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display_without_x_and_y(self):
        """display() prints the rectangle with #."""
        self.assertEqual(self.output(Rectangle(4, 6).display),
                         "####\n" * 6)
        self.assertEqual(self.output(Rectangle(2, 2).display), "##\n##\n")

    def test_display_without_y(self):
        """display() shifts the rectangle by x spaces."""
        self.assertEqual(self.output(Rectangle(3, 2, 1).display),
                         " ###\n ###\n")

    def test_display(self):
        """display() shifts the rectangle by x spaces and y lines."""
        self.assertEqual(self.output(Rectangle(2, 3, 2, 2).display),
                         "\n\n  ##\n  ##\n  ##\n")
        self.assertEqual(self.output(Rectangle(3, 2, 1, 0).display),
                         " ###\n ###\n")

    def test_str(self):
        """__str__ returns [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")
        self.assertEqual(self.output(lambda: print(Rectangle(1, 2))),
                         "[Rectangle] (2) 0/0 - 1/2\n")

    def test_update_args(self):
        """update(89, 2, 3, 4, 5) sets id, width, height, x and y."""
        r = Rectangle(10, 10, 10, 10)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """update(**{'id': 89, ...}) sets attributes by name."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89})
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/10")
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/2")
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(str(r), "[Rectangle] (89) 3/10 - 1/2")
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/2")

    def test_update_args_win(self):
        """kwargs are ignored when positional arguments are given."""
        r = Rectangle(10, 10, 10, 10)
        r.update(5, width=1)
        self.assertEqual(str(r), "[Rectangle] (5) 10/10 - 10/10")

    def test_update_validates(self):
        """update uses the setters, so values are validated."""
        r = Rectangle(10, 10)
        with self.assertRaises(TypeError):
            r.update(1, "2")
        with self.assertRaises(ValueError):
            r.update(height=0)

    def test_to_dictionary(self):
        """to_dictionary() returns all the attributes."""
        r = Rectangle(10, 2, 1, 9)
        self.assertEqual(r.to_dictionary(),
                         {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        r2 = Rectangle(1, 1)
        r2.update(**r.to_dictionary())
        self.assertEqual(str(r2), str(r))
        self.assertIsNot(r, r2)

    def test_save_to_file(self):
        """Rectangle.save_to_file and load_from_file round-trip."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertEqual(str(Rectangle.load_from_file()[0]),
                         "[Rectangle] (1) 0/0 - 1/2")


if __name__ == "__main__":
    unittest.main()
