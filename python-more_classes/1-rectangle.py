#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Rectangle width (default 0)
            height (int): Rectangle height (default 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation.

        Args:
            value (int): width value

        Raises:
            TypeError: if width is not an integer
            ValueError: if width < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation.

        Args:
            value (int): height value

        Raises:
            TypeError: if height is not an integer
            ValueError: if height < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
