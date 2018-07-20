# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 21:57:21 2018

@author: evan9
"""

import string

count = {}
with open(r'c:\PyCodes\File\word_count.txt') as file:
    text = file.read()
    text = text.translate(text.maketrans('','',string.punctuation))
    text = text.lower()
    
    for char in text:
        if char not in string.ascii_lowercase: continue
        count[char] = count.get(char, 0) + 1

byalpha = sorted(count.items())
print('Alphabetical order')
for key,value in byalpha:
    print(key,value)
    
print('')
print('Most Frequent')
bycount = sorted([(value,key) for key,value in count.items()], reverse=True)
for value,key in bycount:
    print(key,value)


'''
String Methods
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
hexdigits = '0123456789abcdefABCDEF'
octdigits = '01234567'
printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
whitespace = ' \t\n\r\x0b\x0c'
'''