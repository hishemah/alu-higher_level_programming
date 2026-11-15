#!/usr/bin/python3
"""Unittests for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """The maximum is found in an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """The maximum is found in an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """The maximum is found at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """The maximum is found in the middle of the list."""
        self.assertEqual(max_integer([1, 5, 2]), 5)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Calling without an argument returns None."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """A list of one element returns that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Negative numbers are compared correctly."""
        self.assertEqual(max_integer([-4, -2, -7]), -2)

    def test_mixed_signs(self):
        """Positive and negative numbers are compared correctly."""
        self.assertEqual(max_integer([-1, 0, 6, -10]), 6)

    def test_duplicates(self):
        """Repeated values return that value."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        """Floats are compared correctly."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_ints_and_floats(self):
        """Integers and floats can be mixed."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_string(self):
        """A string returns its greatest character."""
        self.assertEqual(max_integer("School"), "o")

    def test_list_of_strings(self):
        """A list of strings returns the greatest string."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_list_of_lists(self):
        """A list of lists returns the greatest list."""
        self.assertEqual(max_integer([[1, 2], [3]]), [3])

    def test_none(self):
        """None is not a list."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_types(self):
        """Values that can't be compared raise a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])


if __name__ == '__main__':
    unittest.main()
