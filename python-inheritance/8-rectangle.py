#!/usr/bin/python3
"""Rectangle class inheriting from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height

        Args:
            width (int): The width of the rectangle (must be positive integer)
            height (int): The height of the rectangle (must be positive integer)

        Note:
            - width and height are private (no getter/setter)
            - Both values are validated using integer_validator from BaseGeometry
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
