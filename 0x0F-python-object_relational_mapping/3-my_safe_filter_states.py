#!/usr/bin/python3

"""This script takes in arguments and displays the values in the 'states' table
of 'hbtn_0e_0_usa' where name matches the argument and is safe from
MySQL injections"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = sys.argv[4].split(";")
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY\
                states.id".format(query[0]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
