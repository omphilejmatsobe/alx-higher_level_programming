#!/usr/bin/python3

"""
Class that defines a square
"""


class Square:
    """
    Class defining a square
    """
    def __init__(self, size=0, position=0):
        """
        Method to initialize instance attributes
        """

        self.__size = size
        self.__position = position

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
        """
        Method used to retrieve size of the Square object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Method used to set the size of the Square Object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Method used to retrieve the position attribute for Square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Method used to set the position of square 
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        Method used to print a Square
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    if x < (self.size - 1):
                        print("#", end="")
                    else:
                        print("#")
