#!/usr/bin/python3
"""
===================================
module with method inherits_from
===================================
"""


def inherits_from(obj, a_class):
    """Method returns True if obj is an instance of a class
    that inherited from a_class"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
