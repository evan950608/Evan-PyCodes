# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:26:29 2018

@author: evan9
"""

import urllib.request, urllib.parse, urllib.error
import bs4

url = input('Enter url: ')
#http://www.dr-chuck.com/page1.htm

html = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(html, 'html.parser')
#print(type(soup))
#print(soup)

tags = soup('a')    #type(tags) == <class 'list'>
#print(type(tags))
#print(tags)
count = 0
for tag in tags:
    print(tag.get('href', None))
    count += 1
print(count)

#input('Press enter to continue...')