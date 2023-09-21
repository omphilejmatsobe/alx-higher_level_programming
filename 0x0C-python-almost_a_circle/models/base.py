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

    @staticmethod
    def from_json_string(json_string):
        """
         returns the list of the JSON string representation json_string
        """

        if json_string is None or json_string == '[]':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes"""

        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
         returns a list of instances
        """

        file = str(cls.__name__) + ".json"
        try:
            with open(file, "r") as fl:
                list_dictionaries = Base.from_json_string(fl.read())
                return [cls.create(**dicti) for dicti in list_dictionaries]
        except IOError:
            return []
