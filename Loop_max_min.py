# -*- coding: utf-8 -*-
"""
Created on Sat May 19 17:38:17 2018

@author: evan9
"""

#while True:
#    name = input('Who am I?')
#    if name == 'Evan':
#        break
#print('Good job')

#while True:
#    line = input('> ')
#    if line[0] == '#':
#        continue
#    if line == 'done':
#        break
#    print(line)
#print('Completed')


import random    #random.random()    returns x in the interval [0,1)
nums = []
for i in range(10):
    ran = int(random.random() * 10)    #ran in the interval [0,9]
    nums.append(ran)
print('Original:', nums)

#built-in function: max()
largest = None
for j in nums:
    if largest is None or j > largest:
        largest = j
    print('%2d %2d' % (largest, j))
print('largest: {}'.format(largest))







