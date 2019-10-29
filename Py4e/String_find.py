# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:16:46 2018

@author: evan9
"""

#Count
def count_char_in_str(string, find):
    count = 0
    for s in str(string):
        if s == str(find):
            count += 1
    return count

fruit = 'banana'
count = count_char_in_str(fruit, 'a')
print(count)


#Find
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#mbox.txt line 1

atpos = data.find('@')    #@ position
print(atpos)
sppos = data.find(' ', atpos)    #find space position starting from @ position
print(sppos)
host = data[atpos+1 : sppos]
print(host)
pos = data.find('.')
print(data[pos: pos+3])

'''
help(str.find)
S.find(sub[, start[, end]]) -> int
Required: substring sub
Optional: start
if start was included, Optional: end
'''

str_dir =   ['__add__',
             '__class__',
             '__contains__',
             '__delattr__',
             '__dir__',
             '__doc__',
             '__eq__',
             '__format__',
             '__ge__',
             '__getattribute__',
             '__getitem__',
             '__getnewargs__',
             '__gt__',
             '__hash__',
             '__init__',
             '__init_subclass__',
             '__iter__',
             '__le__',
             '__len__',
             '__lt__',
             '__mod__',
             '__mul__',
             '__ne__',
             '__new__',
             '__reduce__',
             '__reduce_ex__',
             '__repr__',
             '__rmod__',
             '__rmul__',
             '__setattr__',
             '__sizeof__',
             '__str__',
             '__subclasshook__',
             'capitalize',
             'casefold',
             'center',
             'count',
             'encode',
             'endswith',
             'expandtabs',
             'find',
             'format',
             'format_map',
             'index',
             'isalnum',
             'isalpha',
             'isdecimal',
             'isdigit',
             'isidentifier',
             'islower',
             'isnumeric',
             'isprintable',
             'isspace',
             'istitle',
             'isupper',
             'join',
             'ljust',
             'lower',
             'lstrip',
             'maketrans',
             'partition',
             'replace',
             'rfind',
             'rindex',
             'rjust',
             'rpartition',
             'rsplit',
             'rstrip',
             'split',
             'splitlines',
             'startswith',
             'strip',
             'swapcase',
             'title',
             'translate',
             'upper',
             'zfill']