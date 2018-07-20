# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 18:03:18 2018

@author: evan9
"""

import string

with open(r'c:\PyCodes\File\word_count.txt') as file:
    count = {}
    for line in file:
        line = line.rstrip()
        
        #Remove punctuation characters
        line = line.translate(line.maketrans('','', string.punctuation))
        #str.translate(str.maketrans(fromstr, tostr, deletestr))
        #Replace fromstr with tostr; Replace deletestr with None
        #string.punctuation    '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        
        line = line.lower()
        words = line.split()
        print(line)
        for word in words:
            count[word] = count.get(word, 0) + 1

for key,value in count.items():
    print(key,value)
