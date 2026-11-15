#!/usr/bin/python3
"""This module defines MyList, a list that can print itself sorted."""


class MyList(list):
    """A subclass of list that can print its elements in ascending order."""

    def print_sorted(self):
        """Print the elements of the list sorted, without changing the list."""
        print(sorted(self))
