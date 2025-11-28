#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare inheritance against.

    Returns:
        True if obj inherits from a_class but is not exactly a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
