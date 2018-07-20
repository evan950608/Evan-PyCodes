# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 00:36:09 2018

@author: evan9
"""

name = input("Enter file:")
if len(name) < 1 : name = "c:\\PyCodes\\File\\mbox-short.txt"
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
handle = open(name)

count = {}
for line in handle:
    words = line.split()
    if len(words) < 6 or words[0] != 'From': continue
    hour = words[5].split(':')[0]
#    print(hour)
    count[hour] = count.get(hour, 0) + 1
#print(count)

bycount = sorted([(value,key) for key,value in count.items()], reverse=True)
#print(bycount)
for value,key in bycount:
    print(key,value)

print('')
byhour = sorted([(key,value) for key,value in count.items()])
for key,value in byhour:
    print(key,value)
