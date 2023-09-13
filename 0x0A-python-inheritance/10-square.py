#!/usr/bin/python3
"""
========================
Module with class Square
========================
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square that inherits a rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
