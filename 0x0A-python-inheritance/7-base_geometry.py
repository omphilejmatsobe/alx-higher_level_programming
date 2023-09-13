#!/usr/bin/python3
"""
==============================
Module with class BaseGeometry
==============================
"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """method for area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validation if the  num is an integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
