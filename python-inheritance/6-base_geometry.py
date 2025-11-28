#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class with an unimplemented area() method.
    """

    def area(self):
        """
        Raises an exception indicating the method is not implemented.
        """
        raise Exception("area() is not implemented")
