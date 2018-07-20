# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 20:58:47 2018

@author: evan9
"""


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80 ))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)    #Receive up to 512 characters
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()


##Approach2
#import urllib.request, urllib.parse, urllib.error
#
#url = 'http://data.pr4e.org/romeo.txt'
##url = 'http://www.dr-chuck.com/page1.htm'
#
#fhand = urllib.request.urlopen(url)
#for line in fhand:
#    print(line.decode().strip())
