#!/usr/bin/python3
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>


import sys
import MySQLdb

if __name__ == "__main__":
    """Class to select state"""
    d = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], d = sys.argv[3])
    c = d.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
