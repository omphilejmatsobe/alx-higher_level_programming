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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    if x < (self.size - 1):
                        print("#", end="")
                    else:
                        print("#")


