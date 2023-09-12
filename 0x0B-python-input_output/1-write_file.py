#!/usr/bin/python3

"""
====================================
module of the method number_of_lines
====================================
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters written
    Arguments:
        param1: filename
        param2: text
    Return: number of characters written"""


    i = 0
    with open(filename) as fn:
        for line in fn:
            i += 1
        return i
