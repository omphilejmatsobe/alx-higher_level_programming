#!/usr/bin/python3
"""
say_my_name module
This prints the first and last name

"""


def say_my_name(first_name, last_name=""):
    """Return: the first and last name
    Args:
    param1: str first_name
    param2: str last name
    Raise: TypeError
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
