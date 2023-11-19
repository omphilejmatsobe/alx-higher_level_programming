#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    data = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    data.cursor()
    data.cursor().execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in data.cursor().fetchall()]
