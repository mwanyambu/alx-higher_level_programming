#!/usr/bin/python3

"""
scripts lists all cities names of a specified state argument
"""


import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    mydb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    cursor = mydb.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states\
                   ON cities.state_id = states.id\
                   WHERE states.name = %s ORDER BY cities.id", (sys.argv[4], ))
    rows = cursor.fetchall()
    mycity = []
    for row in rows:
        mycity.append(row[0])
    print(", ".join(mycity))

    cursor.close()
    mydb.close()
