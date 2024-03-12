#!/usr/bin/python3
"""
Takes an argument and matches name with the said
argument in states.
Takes 4 arguments username, passwd, db name and state name searched
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'\
    ORDER BY states.id ASC".format(argv[4]))
    
    lst = cur.fetchall()
    for r in lst:
        if r[1] == argv[4]:
            print(r)
            
    cur.close()
    db.close()