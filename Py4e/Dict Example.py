# -*- coding: utf-8 -*-
"""
Created on Sunday, ‎May ‎13, ‎2018, ‏‎17:51:46

@author: evan9
"""

str1 = 'dictionariesaregood'
list1 = list(str1) # d i c t i o n
dt = dict()
print(str1)
print(type(str1))
print(dt)
print(type(dt))
print(list1)
print(type(list1), '\n')

for ch in list1:
   #print(ch)
   if ch not in dt:
       dt[ch] = 1
   else:
       dt[ch] = dt[ch] + 1
       
dt = sorted(dt.items(), key= lambda x: x[1] ,reverse=True)
print('type(dt)', type(dt))
print(dt)

#for (key,value) in dt.items():
#    print("{} {}".format(key,value))

for (key,value) in dt:
    print("{} {}".format(key,value))