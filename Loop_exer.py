# -*- coding: utf-8 -*-
"""
Created on Mon May 21 16:25:37 2018

@author: evan9
"""

count = 0
total = 0
lvals = []
while True:
    sval = input('Enter a number: ')    #str value
    if sval == 'done': break
    try:
        fval = float(sval)    #float value
    except:
        print('Invalid number')
        continue    #exit this iteration and start at the top
    count += 1
    total += fval
    lvals.append(fval)

avg = total / count
print(lvals)
print('Count:', count)
print('Total:', total)
print('Average:', avg)
print('Maximum:', max(lvals))
print('Minimum:', min(lvals))
