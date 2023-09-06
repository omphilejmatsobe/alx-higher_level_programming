#!/usr/bin/python3
"""
text_indentation module
prints a text with new lines after '.?:'

"""


def text_indentation(text):
    """Returns text with 2 new lines after using '.?:'
    Args:
    param1: input str text
    Raise: TypeError
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    x = 0

    while x < len(text) and text[x] == ' ':
        x += 1

    while x < len(text):
        print(text[x], end='')
        if text[x] == '\n' or text[x] in ".?:":
            if text[x] in ".?:":
                print('\n')
            x += 1
            while x < len(text) and text[x] == ' ':
                x += 1
            continue
        x += 1
