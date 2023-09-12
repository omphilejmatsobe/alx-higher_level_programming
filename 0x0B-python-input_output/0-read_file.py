#!/usr/bin/python3


"""
================================
Module with the method read_file
================================
"""

def read_file(filename=""):

    """Reads a text file UTF and prints to stdout
    Argurments:
        param1: filename
        """

    with open(filename, encoding='UTF-8') as f:
        print(f.read(), end="")
