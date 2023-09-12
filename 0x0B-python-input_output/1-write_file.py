#!/usr/bin/python3


def number_of_lines(filename=""):
    i = 0
    with open(filename) as fn:
        for line in fn:
            i += 1
        return i
