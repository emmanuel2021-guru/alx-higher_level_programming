#!/usr/bin/python3


"""This is a script that lists all cities from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))