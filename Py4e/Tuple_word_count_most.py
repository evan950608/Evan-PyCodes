# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 23:17:46 2018

@author: evan9
"""

with open(r'c:\PyCodes\File\word_count.txt') as file:
    count = {}
    for line in file:
        words = line.split()
        for word in words:
            count[word] = count.get(word, 0) + 1
    
    byvalue = []
    for key,value in count.items():
        tup = (value,key)
        byvalue.append(tup)
    byvalue = sorted(byvalue, reverse=True)
    for value,key in byvalue[:10]:
        print(key,value)
        
    #list comprehension
    byvalue2 = sorted([(value,key) for key,value in count.items()], reverse=True)
    