# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 22:54:18 2018

@author: evan9
"""

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
#*** send SQL commands and receive responses through a cursor***
cur = conn.cursor()
### Delete 'emaildb.sqlite' if it already exists ###
cur.execute('DROP TABLE IF EXISTS Tally')

cur.execute('CREATE TABLE Tally (email TEXT, count INTEGER)')

fname = r'c:\PyCodes\File\mbox-short.txt'
fhand = open(fname)

for line in fhand:
    if not line.startswith('From: '): continue
    #From: stephen.marquard@uct.ac.za
    #From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    words = line.split()
    email = words[1]
    
    cur.execute('SELECT count FROM Tally WHERE email = ? ', (email,))
    row = cur.fetchone()
    
    if row is None:
        cur.execute('INSERT INTO Tally (email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Tally SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
### Sort rows by value (descend order) ###
sql_str = 'SELECT email, count FROM Tally ORDER BY count DESC'

for row in cur.execute(sql_str):
    print(row[0], row[1])

cur.close()
fhand.close()