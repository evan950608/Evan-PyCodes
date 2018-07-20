# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:10:23 2018

@author: evan9
"""

import urllib.request
import bs4
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_91647.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = bs4.BeautifulSoup(html, 'html.parser')

#html format
'''
<tr>
    <td>Leydon</td>
    <td>
        <span class="comments">98</span>
    </td>
</tr>
<tr>
    <td>Ayan</td>
    <td>
        <span class="comments">94</span>
    </td>
</tr>
'''

tags = soup('span')    #type(tags) == <class 'list'>
#nums = []
#for tag in tags:
#    num = int(tag.contents[0])
#    nums.append(num)
#    print('NUM:',num)
#    print('TAG:', tag)
#    print('CLASS:', tag.get('class', None)[0])
#    print('CONTENT:', tag.contents[0])
#    print('ATTIBUTES:', tag.attrs)
#    print('-----')

nums = [int(tag.contents[0]) for tag in tags]
print(nums)

print('')
print('SUM:', sum(nums))
print('COUNT:', len(nums))
print('AVERAGE:', sum(nums)/len(nums))







