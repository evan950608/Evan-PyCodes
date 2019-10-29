# -*- coding: utf-8 -*-
"""
Created on Mon May 14 10:20:58 2018

@author: evan9
"""

'''
#tuple to list
tuple1 = (1,5,4,2,3)
print(tuple1)

list1 = list(tuple1)
print(list1)
list1.sort(reverse = True)
print(list1)
'''


#list to tuple
list2 = [1,5,4,2,3]
tuple2 = tuple(list2)
tuple2.append(8)    #Attribute Error
print(tuple2)
