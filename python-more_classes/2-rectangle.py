#!/usr/bin/python3
""" This is path"""


class Rectangle:
    """This is created class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        """ this is  private instance attribute and arguements"""
        
    @property
    def width(self):
        return self.__width
    """This is property"""

        @width.setter
        def width(self, value):
""" this is protery setter"""

            if not isinstance (value, int):
                raise TypeError("width must be an integer")
                    if value < 0:
                        raise ValueError("width must be >= 0")
                    self.__width = value

@property
def height(self):
    return self.__height
""" again property"""

@height.setter
def height(self, value):
    
    if not isinstance (value, int):
        raise TypeError("height must be integer"):
            if value < 0:
raise ValueError("height must be >= 0")
self.__height = value
def area(self):
    return self.width * self.height
def perimeter(self):

    if self.width == 0 or self.height == 0:
        terutn 0
        return 2 * (self.width + self.height)
