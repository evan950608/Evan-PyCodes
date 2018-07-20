# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:21:52 2018

@author: evan9
"""

import random

time0 = 0
time1 = 0
timetry = 0
k = 10
sumtimetry = 0


while time0 != 500 and time1 != 500:
    time0 = 0
    time1 = 0
    for i in range(1000):
        ran = random.choice([0,1])
        if ran == 0:
            time0 += 1
        elif ran == 1:
            time1 += 1
        else:
            print('Neither')
    print('time0= {}'.format(time0))
    print('time1= {}'.format(time1))
    print('---')
    timetry += 1
print('Done, tried {} times'.format(timetry))
