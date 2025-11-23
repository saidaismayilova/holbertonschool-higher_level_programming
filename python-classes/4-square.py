#!/usr/bin/python3
"""4-square.py"""

class Square:
    """Defines a square with private size, getter/setter, area, and print"""

    def __init__(self, size=0):
        """Initialize the square with optional size using the setter for validation"""
        self.size = size  # use setter for validation

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
