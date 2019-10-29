# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:11:42 2018

@author: evan9
"""

'''
Syntax Coloring
Builtin
    default: 
    #aa00aa
Matched Parens
    default: 
    #aa5500
'''

'''
print(abs(-7.6))
print(type(abs(-7)))
print(chr(65))
print(type(chr(65)))
print(divmod(10,3))
print(type(divmod(10,3)))
print(float(8))
print(int(55.98))
print(len([2,5,'an',7.4]))
print(max(2,6,4,8))
print(min(2,6,4,8))
print(pow(3,5,2))
list1 = [2,5,3,7,1]
print(sorted(list1))
#print(sum([1,2,3,4,6.5]))
n = float(input('n= '))
k = int(input('k= '))
print(round(n,k))    #四捨六入 #k(int)為小數位數
'''

list1 = []
ipnum = 0
isum = 0
while ipnum != -1:
    ipnum = int(input('Enter int: '))
    list1.append(ipnum)
list1.pop()

for i in list1:
    isum += i
imax = max(list1)
imin = min(list1)
list2 = sorted(list1, reverse=True)

print('Summation: {}'.format(isum))
print('Maximum: {}'.format(imax))
print('Minimum: {}'.format(imin))
print('From big to small: {}'.format(list2))

#print(type(sum(list1)))





