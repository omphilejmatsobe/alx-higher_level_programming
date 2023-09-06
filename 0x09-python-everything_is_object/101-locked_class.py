#!/usr/bin/python3
"""Defines a class LockedClass"""


class LockedClass:
    """
    Prevents creating new instance attributes,
    except if user fist name is given

    Attributes:
        first_name (str): first name of something.
    """

    __slots__ = ["first_name"]

    def __init__(self):

        """Creates new instances"""

        self.first_name = "first_name"
