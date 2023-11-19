#!/usr/bin/python3
"""
Module states
"""

import sys
import MySQLdb


if __name__ == "__main__":
    """
    This is the module for the database collection of data
    """

    d = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], d=sys.argv[3])
    c = d.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
