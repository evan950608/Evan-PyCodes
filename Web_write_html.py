# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 10:47:20 2018

@author: evan9
"""

import urllib.request, urllib.parse, urllib.error


url = input('Enter url: ')
#http://www.dr-chuck.com/page1.htm

html = urllib.request.urlopen(url).readlines()
with open(r'c:\PyCodes\File\_temp1.html', 'w') as file:
    for line in html:
#        print(line.decode().rstrip())
        file.write(line.decode())
        
