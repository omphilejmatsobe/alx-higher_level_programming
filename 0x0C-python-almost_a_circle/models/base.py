#!/usr/bin/python3

"""
======================
Module with class Base
======================
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        that returns the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
