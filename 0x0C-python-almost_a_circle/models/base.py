#!/usr/bin/python3

"""
======================
Module with class Base
======================
"""


class Base:
    """Class Base for the Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor init
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
