#!/usr/bin/python3
"""Module that defines a Rectangle class with geometry utilities.
"""


class Rectangle:
    """Defines a rectangle shape with width, height, and utility methods.

    Public class attributes:
        number_of_instances (int): Count of active Rectangle instances.
        print_symbol: Symbol used for printing the Rectangle.

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle perimeter.

        Returns:
            0 if width or height is zero.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a printable string representation using print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        sym = str(self.print_symbol)
        return "\n".join(sym * self.width for _ in range(self.height))

    def __repr__(self):
        """Return a string capable of recreating the Rectangle instance."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Called when a Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the larger area.

        Args:
            rect_1 (Rectangle)
            rect_2 (Rectangle)

        Returns:
            rect_1 if both areas are equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def
