#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a class or a class that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or any class
    that inherited from a_class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True or False.
    """
    return isinstance(obj, a_class)
