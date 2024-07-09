#!/usr/bin/python3

"""
Class that defines a square
"""


class Square:
    """
    Class defining a square
    """
    def __init__(self, size=0):
        """
        Method to initialize instance attributes
        """

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            pass

    def area(self):
        """
        Method that return area of Square object
        """
        return (self.__size * self.__size)
