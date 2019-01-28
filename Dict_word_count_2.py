# -*- coding: utf-8 -*-
"""
Created on Tue May 29 20:24:48 2018

@author: evan9
"""

name = input("Enter file:")
if len(name) < 1:
    name = "C:\\Users\\evan9\\OneDrive\\Document\\GitHub\\Evan-Python-Basics\\File\\mbox-short.txt"
handle = open(name)

counts = {}
emails = []
for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != 'From': continue
    email = words[1]
    emails.append(email)

#print(emails)
for email in emails:
    counts[email] = counts.get(email, 0) + 1

bigemail = None
bigcount = None
for key,value in counts.items():
    if bigcount is None or value > bigcount:
        bigcount = value
        bigemail = key
print(bigemail, bigcount)
