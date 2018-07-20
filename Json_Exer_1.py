# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:08:40 2018

@author: evan9
"""

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_91650.json'

data = urllib.request.urlopen(url, context=ctx).read().decode()
js = json.loads(data)

summ = 0
for person in js['comments']:
    summ += int(person['count'])
    
print('Sum:', summ)
print('Count:', len(js['comments']))
print('Average:', summ/len(js['comments']))