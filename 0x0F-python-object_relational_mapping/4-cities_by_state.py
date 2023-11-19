#!/usr/bin/python3

"""
script lists all cities
"""


import sys
import MySQLdb

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    mydb = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = mydb.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                   FROM cities JOIN states WHERE cities.state_id = states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    mydb.close()
