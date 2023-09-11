#!/usr/bin/python3
def is_same_class(obj, a_class):
    """checks if obj is the same class
    Arguments:
        param1: input obj
        param2:  input a_class that matches the obj
    Return:
    True for isinstance of obj or False if not
    """

    if type(obj) == a_class:
        return True
    else:
        return False
