#!/usr/bin/python3

"""
script lists all states from hbtn_0e_0_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)
    username, password, database = sys.argv[1:4]

    mydb = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database)
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    mydb.close()
