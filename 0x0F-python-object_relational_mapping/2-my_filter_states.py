#!/usr/bin/python3

"""
script filters table with the specified state name
"""


import sys
import MySQLdb

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    mydb = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM states\
                   WHERE states.name LIKE BINARY '{}'\
                   ORDER BY states.id".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    mydb.close()
