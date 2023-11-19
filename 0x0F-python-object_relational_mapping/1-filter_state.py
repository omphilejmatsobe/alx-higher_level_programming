#!/usr/bin/python3
"""
module for state filtering
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """
    this filters the state date
    """
    d = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], d=sys.argv[3])
    cur = d.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
