#!/usr/bin/python3
"""
Module states
"""

import sys
import MySQLdb


if __name__ == "__main__":
    """
    This is the module for the database collection
    """

    d = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cur.execute("SELECT * FROM states")

    i = cursor.fetchall()
    for x in i:
        print(x)

    cur.close()
    db.close()
