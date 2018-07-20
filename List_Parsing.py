# -*- coding: utf-8 -*-
"""
Created on Sun May 27 12:08:02 2018

@author: evan9
"""

#infile = open(r'c:\PyCodes\File\romeo.txt')
#allwords = []
#
#for line in infile:
#    words = line.split()
#    for word in words:
#        if word in allwords:
#            pass
#        else:
#            allwords.append(word)
#allwords.sort()
#print(allwords)


import os.path

while True:
    fname = input('Enter file name: ')
    #c:\\PyCodes\\File\\mbox-short.txt
    is_exists = os.path.isfile(fname)    #type(is_exists) == 'bool'
    
    if is_exists:
        infile = open(fname)
        break
    else:
        print('File cannot be opened:',fname)
        continue
    
count = 0
for line in infile:
    words = line.split()
    if len(words) < 2 or words[0] != 'From': continue
    count += 1
    email = words[1]
#    name = ' '.join(email.split('@')[0].split('.')).capitalize()
    print (email)
print(count)




