#!/usr/bin/python3

"""This script lists all the states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    arg = sys.argv[4].split(";")
    cur.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC"
                .format(arg[0]))
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
