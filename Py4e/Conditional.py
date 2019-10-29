# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:52:49 2018

@author: evan9
"""

score = float(input('Score: '))
if score<=1:
    if score>=0.9:
        print('A')
    elif score>=0.8:
        print('B')
    elif score>=0.7:
        print('C')
    elif score>=0.6:
        print('D')
    else:
        print('F')
else:
    print('Score must be between 0.0 and 1.0')
