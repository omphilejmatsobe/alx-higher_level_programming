#!/usr/bin/python3

"""
=====================================
Module with the method to_json_string
=====================================
"""

import json

def to_json_string(my_obj):
        """returns the JSON representation of an object
    Arguments:
        param1: my_obj
    Return: json representation"""

    return json.dumps(my_obj)
