#!/usr/bin/python3

"""
=================================
Module with the method read_lines
=================================
"""


def read_lines(filename="", nb_lines=0):
    """appends a string at the end of a text file and returns the number of characters added
    Arguments:
        param1: filename
        param2: nb_lines
    Return: number of characters added"""

    with open(filename, encoding="UTF-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return

        i = 0
        for line in f:
            i += 1
        f.seek(0)
        if nb_lines >= ln:
            print(f.read(), end="")
            return
        else:
            j = 0
            while j < nb_lines:
                print(f.readline(), end="")
                j += 1
