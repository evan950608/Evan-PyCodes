# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 16:30:44 2018

@author: evan9
"""

import urllib.request
import bs4
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = []
urls.append(input('Enter url: '))
#http://py4e-data.dr-chuck.net/known_by_Fikret.html
#http://py4e-data.dr-chuck.net/known_by_Anne.html
pos = int(input('Look for position: '))    #(3,18)
rep = int(input('Repetition times: '))     #(4,7)

names = []
html = urllib.request.urlopen(urls[0], context=ctx).read()
soup = bs4.BeautifulSoup(html, 'html.parser')
oriname = soup('h1')[0].contents[0].split()[2]
names.append(oriname)
print(names)

for i in range(rep):
    html = urllib.request.urlopen(urls[i], context=ctx).read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    
    #Get pos(th) link and append to urls
    url_next = tags[pos - 1].get('href', None)
    urls.append(url_next)
#    print(urls)
    
    #Get pos(th) name and append to names
    name = tags[pos - 1].contents[0]
    names.append(name)
    print(names)
    
for name in names:
    print(name)
    
    
    
    