#!/usr/bin/python3
"""
Safe from SQL injections
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    check = (argv[4], )
    cur.execute("SELECT * FROM states WHERE name = %s\
    ORDER BY states.id ASC", check)

    lst = cur.fetchall()
    for r in lst:
        print(r)

    cur.close()
    db.close()