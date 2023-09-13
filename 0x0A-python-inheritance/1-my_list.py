#!/usr/bin/python3

"""
=============================
Module with the method MyList
=============================
"""


class MyList(list):
    """module inherits methods from list
    Arguments:
        param1: list"""

    def print_sorted(self):
        print(sorted(self))
