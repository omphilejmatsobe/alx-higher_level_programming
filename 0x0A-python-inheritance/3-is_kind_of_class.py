#!/usr/bin/python3


"""
===================================
module with method is_kind_of_class
===================================
"""


def is_kind_of_class(obj, a_class):
    """function checks if obj is the same kind of class
    Arguments:
        param1: obj
        param2: a_class thats the same as obj
    Return:
    True for isinstance of obj or False if not
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
