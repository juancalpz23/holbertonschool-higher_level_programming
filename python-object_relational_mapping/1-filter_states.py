#!/usr/bin/python3
"""
List all states with a name starting with 'N'
Should take 3 arguments username, passwd and db name
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                 ORDER BY id ASC;")
    
    lst = cur.fetchall()
    for r in lst:
        if r[1][0] == 'N':
            print(r)

    cur.close()
    db.close()
