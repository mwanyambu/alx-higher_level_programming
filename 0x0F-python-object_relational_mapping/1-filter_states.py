#!/usr/bin/python3

"""
scripts filters states that start with a specified letter
"""


import sys
import MySQLdb

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    mydb = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM states\
                   WHERE states.name like 'N%' ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    mydb.close()
