# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 23:10:28 2018

@author: evan9
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_91649.xml'

data = urllib.request.urlopen(url).read()    #full xml
tree = ET.fromstring(data.decode())
#data format
'''
<comment>
    <name>Jai</name>
    <count>99</count>
</comment>
<comment>
    <name>Martyna</name>
    <count>99</count>
</comment>
'''

sum = 0
comments = tree.findall('comments/comment')
for comment in comments:
    name = comment.find('name').text
    count = int(comment.find('count').text)
    print('Name: {0}, Count: {1}'.format(name,count))
    sum += count
print('Sum:',sum)


