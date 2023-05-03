#!/usr/bin/python3


"""This is a script that lists all cities from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
<<<<<<< HEAD
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities INNER JOIN states ON \
            cities.state_id = states.id ORDER BY cities.id")
    rows = cur.fetchall()
=======
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT *  FROM  cities INNER JOIN states ON state_id ORDER id")
    rows = c.fetchall()
>>>>>>> 994bb9006de3b7a182cbe67b661c32ed35d14c22
    for row in rows:
        print("{}".format(row))
