# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 22:05:43 2018

@author: evan9
"""

name = input("Enter file:")
if len(name) < 1 : name = "c:\\PyCodes\\File\\mbox-short.txt"
handle = open(name)

counts = {}
emails = []
for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != 'From': continue
    email = words[1]
    emails.append(email)

for email in emails:
    counts[email] = counts.get(email, 0) + 1

#print(counts)
byvalue = sorted([(value,key) for key,value in counts.items()], reverse=True)
#print(byvalue)

for value,key in byvalue:
    print(key,value)