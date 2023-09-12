#!/usr/bin/python3

import json


"""
=====================================
Module with the method to_json_string
=====================================
"""

def to_json_string(my_obj):
        """returns the JSON representation of an object
    Arguments:
        param1: my_obj
    Return: json representation"""

    return json.dumps(my_obj)
