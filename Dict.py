# -*- coding: utf-8 -*-
"""
Created on Mon May 14 10:30:09 2018

@author: evan9
"""

dict1 = {'Arthur':85, 'Bill':80, 'Charles':72}
dict1['David'] = 90
'''
print(len(dict1))
print(dict1)

n = dict1.get('Arthur')
print(n)

b = 'Evan' in dict1
print(b)

dict2 = dict1.keys()
print(dict2)
list2 = list(dict2)
print('Keys: {}'.format(list2))

n2 = dict1.setdefault('Bill')
print(n2)

dict3 = dict1.values()
print(dict3)
list3 = list(dict3)
print('Value: {}'.format(list3))
'''
print('Approach 1')
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print('{}\'s score is {}'.format(listkey[i],listvalue[i]))

print('\n','Approach 2')
listitems = dict1.items()
for key,value in listitems:
    print('{}\'s score is {}'.format(key,value))

print('\n') #get
n1 = dict1.get('David')
print(n1)
n2 = dict1.get('David',100)
print(n2)
n3 = dict1.get('Evan')
print(n3)
n4 = dict1.get('Evan',100)    #100 is the default value for key'Evan'
print(n4)

print('\n') #setdefault
n5 = dict1.setdefault('Bill')
print(n5)
print(dict1)
n6 = dict1.setdefault('Bill',100)
print(n6)
print(dict1)
n7 = dict1.setdefault('Fred')
print(n7)
print(dict1)
n8 = dict1.setdefault('George',100)
print(n8)
print(dict1)





