# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 22:43:37 2018

@author: evan9
"""

score = {'Bill':70, 'Charles':90, 'Arthur': 80}

for key,value in sorted(score.items()):    #loop through the dict in key order
    print(key,value)
    
byvalue = []
for key,value in score.items():    #loop through the dict in value order
    tup = (value, key)
    byvalue.append(tup)
byvalue = sorted(byvalue, reverse=True)
print(byvalue)

for value,key in byvalue:
    print(key,value)