#!/usr/bin/python3
"""
List all states from db hbtn_0e_usa
Takes 3 args mysql username, mysql passwd, db name
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    lst = cur.fetchall()
    for r in lst:
        print(r)
    cur.close()
    db.close()