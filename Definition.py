# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:24:27 2018

@author: evan9
"""

def hello():
    print('Hello World')
def GetArea(w,l=8):    #default l=8
    area = w * l
    return area
def ctof(c):
    f = 1.8 * c + 32
    return f
def ftoc(f):
    c = (5/9)*(f - 32)
    return c
def add(*k):
    sum = 0
    for i in k:
        sum += i
    return sum
def scope():
    global var1
    var1 = 1
    var2 = 2
    print(var1,var2)
#hello()
'''
a = GetArea(float(input('width=')),float(input('length=')))
print('Area= {}'.format(a))

ipc = float(input('Degree in Celcius: '))
retf = ctof(ipc)
print('Convert to Fahrenheit： {}'.format(retf))

ipf = float(input('Degree in Fahrenheit: '))
retc = ftoc(ipf)
print('Convert to Celcius: {}'.format(retc))
'''

retsum = add(60,80,70)
print(retsum)

var1 = 10
var2 = 20
scope()
print(var1,var2)