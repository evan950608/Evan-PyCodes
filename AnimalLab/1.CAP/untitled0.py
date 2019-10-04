# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:33:41 2019

@author: evan9
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rfile = open('test.txt')

i = 0
data = pd.DataFrame(columns=['Time', 'Ch1', 'Ch2'])
for line in rfile:
    if line.startswith('-0') or line.startswith('0'):
#        print(line.rstrip().split('\t'))
        data.loc[i] = line.rstrip().split('\t')
        i += 1
print(i)

max(data['Ch2'])



# In[]
df = pd.DataFrame(columns=['Time', 'Ch1', 'Ch2'])
df.loc[0] = ['a', 'b', 'c']
df.loc[1] = ['d', 'e', 'f']

from robert import preprocessor as pp
social = pp.dataset('Social_Network_Ads.csv')

a = 'abc interval def interval ghi'
lst = a.split(' interval ')
print(lst)







