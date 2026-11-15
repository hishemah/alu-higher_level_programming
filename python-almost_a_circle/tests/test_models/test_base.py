#!/usr/bin/python3
"""Unittests for models/base.py."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset the automatic id counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove the files the tests may have written."""
        for name in ("Base.json", "Rectangle.json", "Square.json",
                     "Rectangle.csv", "Square.csv"):
            if os.path.exists(name):
                os.remove(name)

    def test_automatic_id(self):
        """Base() gets the next automatic id."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_given_id(self):
        """Base(89) keeps the id 89 and doesn't use the counter."""
        self.assertEqual(Base(89).id, 89)
        self.assertEqual(Base().id, 1)

    def test_id_none(self):
        """Base(None) gets an automatic id."""
        self.assertEqual(Base(None).id, 1)

    def test_other_ids(self):
        """Any non None value is used as the id."""
        self.assertEqual(Base(-5).id, -5)
        self.assertEqual(Base("id").id, "id")

    def test_private_counter(self):
        """The counter is not reachable by its plain name."""
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_to_json_string_none(self):
        """to_json_string(None) returns "[]"."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """to_json_string([]) returns "[]"."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        """to_json_string([{'id': 12}]) returns a JSON string."""
        result = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(result, str)
        self.assertEqual(result, '[{"id": 12}]')

    def test_to_json_string_rectangle(self):
        """A rectangle dictionary round-trips through JSON."""
        d = Rectangle(10, 7, 2, 8, 1).to_dictionary()
        self.assertEqual(json.loads(Base.to_json_string([d])), [d])

    def test_from_json_string_none(self):
        """from_json_string(None) returns []."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """from_json_string("[]") returns []."""
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string(self):
        """from_json_string('[{ "id": 89 }]') returns the list."""
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'),
                         [{"id": 89}])

    def test_save_to_file_none(self):
        """Rectangle.save_to_file(None) writes "[]"."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Rectangle.save_to_file([]) writes "[]"."""
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file(self):
        """Rectangle.save_to_file([Rectangle(1, 2)]) writes its JSON."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json") as f:
            self.assertEqual(json.loads(f.read()),
                             [{"x": 0, "y": 0, "id": 1,
                               "height": 2, "width": 1}])

    def test_save_to_file_square(self):
        """Square.save_to_file([Square(1)]) writes its JSON."""
        Square.save_to_file([Square(1)])
        with open("Square.json") as f:
            self.assertEqual(json.loads(f.read()),
                             [{"id": 1, "x": 0, "size": 1, "y": 0}])

    def test_save_to_file_overwrites(self):
        """Saving again replaces the content of the file."""
        Square.save_to_file([Square(1), Square(2)])
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_create_rectangle(self):
        """Rectangle.create(**{'id': 89, ...}) sets all the attributes."""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual((r.id, r.width), (89, 1))
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/2")
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(str(r), "[Rectangle] (89) 3/0 - 1/2")
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2,
                                'x': 3, 'y': 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_create_square(self):
        """Square.create(**{'id': 89, ...}) sets all the attributes."""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(str(s), "[Square] (89) 2/0 - 1")
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_create_is_a_new_instance(self):
        """create returns a different object with the same values."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_load_from_file_no_file(self):
        """load_from_file() returns [] when the file doesn't exist."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file(self):
        """load_from_file() returns the saved instances."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual([str(r) for r in loaded], [str(r1), str(r2)])
        self.assertIsInstance(loaded[0], Rectangle)

    def test_load_from_file_square(self):
        """load_from_file() returns the saved squares."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual([str(s) for s in loaded], [str(s1), str(s2)])
        self.assertIsInstance(loaded[1], Square)

    def test_csv_round_trip(self):
        """save_to_file_csv and load_from_file_csv keep all values."""
        rectangles = [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]
        squares = [Square(5), Square(7, 9, 1)]
        Rectangle.save_to_file_csv(rectangles)
        Square.save_to_file_csv(squares)
        self.assertEqual([str(r) for r in Rectangle.load_from_file_csv()],
                         [str(r) for r in rectangles])
        self.assertEqual([str(s) for s in Square.load_from_file_csv()],
                         [str(s) for s in squares])

    def test_csv_no_file(self):
        """load_from_file_csv() returns [] when the file doesn't exist."""
        self.assertEqual(Rectangle.load_from_file_csv(), [])


if __name__ == "__main__":
    unittest.main()
