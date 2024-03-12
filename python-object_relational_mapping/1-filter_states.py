#!/usr/bin/python3
"""
List all states with a name starting with 'N'
Should take 3 arguments username, passwd and db name
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    
    curr = db.cursor()

    curr.execute("SELECT * FROM states where name LIKE 'N%'\
                 ORDER BY states.id ASC:")
    
    lst = curr.fetchall()
    for r in lst:
        if r[1][0] == 'N':
            print(r)
            
    curr.close()
    db.close()