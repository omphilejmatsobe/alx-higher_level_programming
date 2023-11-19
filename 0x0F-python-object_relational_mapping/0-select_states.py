#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    d = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    d.cursor()
    d.cursor().execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in d.cursor().fetchall()]
