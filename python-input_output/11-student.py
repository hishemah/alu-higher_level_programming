#!/usr/bin/python3
"""Module that defines a Student class that can be saved and reloaded."""


class Student:
    """Represent a student with a first name, a last name and an age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): the first name of the student.
            last_name (str): the last name of the student.
            age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student.

        Args:
            attrs (list): if it is a list of strings, only the attributes
                named in it are returned; otherwise all are returned.
        """
        if (type(attrs) == list and
                all(type(name) == str for name in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student with those in a dictionary.

        Args:
            json (dict): the attribute names and the values to set.
        """
        for key, value in json.items():
            setattr(self, key, value)
