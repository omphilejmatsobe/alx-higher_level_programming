#!/usr/bin/python3
"""
add_integer
this adds two integers together
"""


def add_integer(a, b=98):
    """Return an integer result for addition of a an b,
    Raise: TypeError
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
