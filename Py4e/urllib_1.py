# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 23:24:34 2018

@author: evan9
"""

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open(r'c:\PyCodes\File\cover3.jpg', 'wb')

size = 0
count = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size += len(info)
    count += 1
    fhand.write(info)

print(size, 'characters copied.')
print('Cycled {0} times.'.format(count))
fhand.close()
