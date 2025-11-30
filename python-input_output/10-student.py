#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary representation of the Student.
        If attrs is a list of strings, return only those attributes.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(type(a) is str for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
