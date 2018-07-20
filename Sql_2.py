# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 12:10:17 2018

@author: evan9
"""

import sqlite3

conn = sqlite3.connect(r'c:\PyCodes\Database\Sql_3.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

i = 0
with open(r'c:\PyCodes\File\mbox.txt') as mbox:
    for line in mbox:
        words = line.split()
        if len(words) < 2 or words[0] != 'From:': continue
        domain = words[1].split('@')[1]
        
        cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
        row = cur.fetchone()
        
        i += 1
        if row is None:
            cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)', (domain,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))
            
        ### Commit every 10 iterations ###
        if i % 10 == 0: conn.commit()
        
conn.commit()
sql_cmd = 'SELECT org,count FROM Counts ORDER BY count DESC'
for row in cur.execute(sql_cmd):
    print(row[0], row[1])

cur.close()


