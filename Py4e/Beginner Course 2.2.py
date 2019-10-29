# -*- coding: utf-8 -*-
"""
Created on Friday, ‎May ‎11, ‎2018, ‏‎21:47:11

@author: evan9
"""

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))


print('\nComparison')
print((a > b) or (a*b > 0))    #'True' or 'False


#Calculate sum and average
grades = [a,b,c]
sum = 0
for i in grades:
    sum += i
print('summation= {}'.format(sum))
average = sum/len(grades)
print('average= {}'.format(average))
