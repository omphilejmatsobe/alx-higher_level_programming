#!/usr/bin/python3

"""
===============================
module of the method write_file
===============================
"""


def write_file(filename="", text=""):
    """Writes a string to a text, returns the number of characters written
    Arguments:
        param1: filename
        param2: text
    Return: number of characters written"""

    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
