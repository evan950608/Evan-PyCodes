# -*- coding: utf-8 -*-
"""
Created on Wed May 16 20:45:49 2018

@author: evan9
"""

str1 = 'Evan'
try:
    print('Hello')    #run
    a = int(str1)     #TypeError, does not run
    print('There')    #does not run
except:
    a = -1            #run
print('Done',a)       #Done -1

#str2 = '-3.2'
#print(int('5'))

inp = input('Please enter an integer: ')
#print(type(inp))
try:
    inpint = int(inp)
except:
    inpint = 1.1
if inpint != 1.1:
    print('Good')
else:
    print('Not an integer')
