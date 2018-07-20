# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 11:22:40 2018

@author: evan9
"""

import json
import sqlite3

conn = sqlite3.connect(r"C:\PyCodes\Database\rosterdb.sqlite")
cur = conn.cursor()

### Set up database ###
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;
''')
cur.executescript('''
CREATE TABLE User (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE);

CREATE TABLE Course (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title   TEXT UNIQUE);

CREATE TABLE Member (
    user_id      INTEGER,
    course_id    INTEGER,
    role         INTEGER,
    PRIMARY KEY  (user_id, course_id));
''')
#set (user_id, course_id) conbination into an unique key

fname = r"C:\PyCodes\Py4e Sample Code\roster\roster_data_sample.json"
with open(fname) as file:
    data_str = file.read()
    data_json = json.loads(data_str)
    
for user in data_json:
#    name = user[0]
#    title = user[1]
#    role = user[2]
    (name, title, role) = user
    print(user)
    
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]
    
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role)
                   VALUES (?,?,?)''', (user_id, course_id, role))
    
    conn.commit()
    
cur.close()
    
    
### Visualize ###
'''
SELECT User.name, Course.title, Member.role 
FROM User JOIN Course JOIN Member
ON Member.course_id = Course.id 
AND Member.user_id = User.id
ORDER BY Course.title, Member.role DESC, User.name;
'''
    
    
    
    
    
    
    







