#!/usr/bin/python3

"""
======================================
Module with the method number_of_lines
======================================
"""


def number_of_lines(filename=""):
    """Writes a string to a text file and returns the number of characters written
    Arguments:
        param1: filename
    Return: number of characters written"""

    i = 0
    with open(filename) as fn:
        for line in fn:
            i += 1
        return i
