# -*- coding: utf-8 -*-
"""
Created on Fri May 18 19:40:33 2018

@author: evan9
"""

#xfile = open('c:\\PyCodes\\File\\test1.txt')
xfile = open(r'c:\PyCodes\File\test1.txt')
#r' ': There are no Escape Characters

'''
count = 0
for line in xfile:
#    print(line)
    count += 1
print('Line count: {}'.format(count))
'''


#Searching through a file_Approach1
for line in xfile:
    line = line.rstrip()    #strip off whitespaces,newlines at the end of each line
    if line.startswith('From:'):
        print(line)
     
'''     
#Approach2_Skipping with Continue
for line in xfile:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)    #"print" command needs to put behind "if" command
'''

