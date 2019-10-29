# -*- coding: utf-8 -*-
"""
Created on Fri May 11 20:18:20 2018

@author: evan9
"""

name = 'Evan'
grade1 = 88
grade2 = 1235589.855

#print('%s' % ())
#'%s':str, '%d':int, '%f':float
print('%s\'s score is %d' % (name, grade1))
print('%s\'s score is %8.2f' % (name, grade2))    #8 characters; 2 decimal digits
print('%s\'s score is %5d' % (name, grade1))    #5 characters

#print('{}'.format())
print('{}\'s score is {}'.format(name, grade1))
num1 = 1234567.126
print('{:,}'.format(num1))    #1,234,567.126
print('{0:,.2f}---{1:,.2f}---{0:,.2f}'.format(num1,2345))
s = '{0}\'s score is {1}'.format(name,grade1)
print(s)

names = ['Arthur','Bill','Charles']
num2 = 5 + 6.8
print(num2,type(num2))    #float
num3 = 5 + True
print(num3,type(num3))    #int
print(int(num2))
print(float(num3))
print(str(num3))

