# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:31:57 2018

@author: evan9
"""

#Digits in Fibonacci Sequence
k = int(input('Digits in Fibonacci Sequence: '))

list1 = [1,1]
for i in range(k - 2):
    list1.append(list1[i] + list1[i+1])
for j in list1:
    print(j)

