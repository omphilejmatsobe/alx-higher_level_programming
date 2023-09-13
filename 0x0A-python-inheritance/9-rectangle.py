#!/usr/bin/python3
"""
==============================
Module with class of Rectangle
==============================
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that  inherits BaseGeometry"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):

        _str = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

        return _str
