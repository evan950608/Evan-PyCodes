# -*- coding: utf-8 -*-
"""
Created on Fri May 18 21:36:18 2018

@author: evan9
"""

#xfile = open(r'c:\PyCodes\File\test1.txt')

try:
    inpname = input('Enter file name: ')
    #c:\\PyCodes\\File\\filename.txt
    xfile = open(inpname)
except:
    print('File cannot be opened:', inpname)
    input('Press Enter to continue...')
#    quit()
    exit()
    
count = 0
for line in xfile:
    if line.startswith('From:'):
        count += 1
    
print('There are {} lines which start with \'From\':'.format(count))
input('Press Enter to continue...')
