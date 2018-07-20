# -*- coding: utf-8 -*-
"""
Created on Saturday, ‎May ‎12, ‎2018, ‏‎17:09:56

@author: evan9
"""

'''
Discount rate:
    origprice < 1000, r = 1
    1000 <= origprice < 1500, r = 0.9
    1500 <= origprice < 2000, r = 0.8
    origprice >= 2000, r = 0.7
'''

origprice = int(input('Please enter original price: '))

'''
#Approach_1
if(origprice >= 1000):
    if(origprice >= 2000):
        r = 0.7
        n = origprice*r
        print('Discount rate= {}'.format(r))
        print('After discount: ${:,}'.format(n))
    elif(origprice >= 1500):
        r = 0.8
        n = origprice*r
        print('Discount rate= {}'.format(r))
        print('After discount: ${:,}'.format(n))
    else:
        r = 0.9
        n = origprice*r
        print('Discount rate= {}'.format(r))
        print('After discount: ${:,}'.format(n))
else:
    r = 1
    n = origprice*r
    print('Discount rate= {}'.format(r))
    print('After discount: ${:,}'.format(n))
'''

#Approach_2
def decide_rate(p):
    if(p >= 1000):
        if(p >= 2000):
            r = 0.7
        elif(p >= 1500):
            r = 0.8
        else:
            r = 0.9
    else:
        r = 1.0
    return r
def calc_discount(p, r):
    n = p * r
    return n

rate = decide_rate(origprice)
disprice = calc_discount(origprice, rate)
print('Discount rate: {}'.format(rate))
print('After discount: ${:,}'.format(disprice))








