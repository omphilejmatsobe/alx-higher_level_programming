#!/usr/bin/python3

"""
=================================
Module with the method read_lines
=================================
"""


def append_write(filename="", text=""):
    """returns the JSON representation of an object
    Arguments:
        param1: filame
        param2: text
    Return: JSON representation"""

    with open(filename, "a", encoding="UTF-8") as fn:
        return fn.write(text)
