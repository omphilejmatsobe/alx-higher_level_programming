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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves json object to file.
        """

        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as J:
            J.write(cls.to_json_string(list_objs))
