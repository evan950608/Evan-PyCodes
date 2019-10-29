# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 15:31:00 2018

@author: evan9
"""

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect(r"C:\PyCodes\Database\trackdb_2.sqlite")
cur = conn.cursor()

### Set up database ###
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
''')

cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER);
''')

fname = r"C:\PyCodes\Py4e Sample Code\tracks\Library.xml"

def lookup(parent, key):
    found = False
    for child in parent:
        if found :
            return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

tree = ET.parse(fname)
songs = tree.findall('dict/dict/dict')

written = 0
skipped_1 = 0
skipped_2 = 0
for song in songs:
    ### make sure song has Track ID ###
    if lookup(song, 'Track ID') is None:
        skipped_1 += 1
        continue
    
    name = lookup(song, 'Name')
    artist = lookup(song, 'Artist')
    album = lookup(song, 'Album')
    genre = lookup(song, 'Genre')
    count = lookup(song, 'Play Count')
    rating = lookup(song, 'Rating')
    length = lookup(song, 'Total Time')
    
    info = (name, artist, album, genre, count, rating , length)
    if None in info:
        skipped_2 += 1
        continue
    print(info)
    
    written += 1
    ### Write to TABLE Artist ###
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES ( ? )', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]    #.fetchone() returns a '1 object tuple'
    
    ### Write to TABLE Album ###
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]
    
    ### Write to TABLE Genre ###
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cur.fetchone()[0]
    
    ### Write to TABLE Track ###
    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) 
    VALUES ( ?, ?, ?, ?, ?, ? )''', ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()
    
cur.close()
print('Written: {0}, Skipped_1: {1}, Skipped_2: {2}'.format(written, skipped_1, skipped_2))











