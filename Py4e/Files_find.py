# -*- coding: utf-8 -*-
"""
Created on Fri May 18 21:47:00 2018

@author: evan9
"""

xfile = open(r'c:\PyCodes\File\mbox-short.txt')
print(xfile)

count = 0
for line in xfile:
    line = line.rstrip()
#    if '@uct.ac.za' in line:
#        print(line)
#        count += 1
#    if line.find('@uct.ac.za') != -1:
#        print(line)
#        count += 1
    if line.find('@uct.ac.za') == -1:
        continue
    print(line)
    count += 1
    
print('Count= {}'.format(count))
#input('Press Enter to continue...')

#list1 = [1,2]
#help(list1.append)
#line1 = 'abc'
#help(line1.find)