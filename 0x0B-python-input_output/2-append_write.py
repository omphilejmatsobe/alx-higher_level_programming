#!/usr/bin/python3

"""
===================================
Module with the method append_write
===================================
"""

def append_write(filename="", text=""):
        """appends a string at the end of a text file and returns the number of characters added
    Arguments:
        param1: filename
        param2: text
    Return: number of characters added"""

    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text) i

