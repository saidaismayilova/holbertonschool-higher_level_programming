#!/usr/bin/python3
"""1-square.py"""

class Square:
    """Defines a square with a private size attribute and validation"""

    def __init__(self, size=0):
        """Initialize the square with optional size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
