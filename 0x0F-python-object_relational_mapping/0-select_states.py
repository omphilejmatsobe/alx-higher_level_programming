#!/usr/bin/python3
"""
module for the select_state class
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """Class to select state"""
    d = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], d=sys.argv[3])
    c = d.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
