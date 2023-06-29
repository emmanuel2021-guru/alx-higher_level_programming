#!/usr/bin/python3

"""This script takes in the name of a state as an argument and lists all
cities of that state, using the database 'hbtn_0e_4_usa'"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = sys.argv[4].split(";")
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON\
                 cities.state_id = states.id WHERE states.name = '{}'\
                 ORDER BY cities.id".format(query[0]))
    rows = cur.fetchall()
    my_str = ""
    for row in rows:
        if my_str == "":
            my_str += row[0]
        else:
            my_str += ", {}".format(row[0])
    print(my_str)
