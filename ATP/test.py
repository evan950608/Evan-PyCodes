# -*- coding: utf-8 -*-
"""
Created on Tue May 22 20:38:23 2018

@author: evan9
"""

import urllib
import shelve
import bs4

def GetWebPage(url):
    #----simple way
    #html = urllib.request.urlopen(url).read() #url = 'http://www.bbc.com/news/uk-politics-44174575'
    #*****simulate browser*****
    req = urllib.request.Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    html =  urllib.request.urlopen(req).read()
    return html

def GetValidFilename(fname):
    nonvalid_alphabets = [':','\\','/','*','?','"','<','>','|']
    list_alphabet = [s for s in list(fname.strip()) if s not in nonvalid_alphabets]
#    list_alphabet = []
#    for s in list(fname.strip()):
#        if s not in nonvalid_alphabets:
#            list_alphabet.append(s)
    return ''.join(list_alphabet)

def SaveShelveCache(name, value):
    f_shelve = shelve.open('efg')
    f_shelve[name] = value
    f_shelve.close()

def GetShelveCache(name):    
    try:
        shelveCache = shelve.open('cache')
        return shelveCache[name]
    except:
        return None

def main():
    #*****ATP News************   
    #*** Load Web Page ****
    url = 'http://www.atpworldtour.com/en'
    html = GetWebPage(url)
#    fname = GetValidFilename(' a<>aa.html ')
#    print(fname)
#    f = open(fname , 'wb')
#    f.write(r)
#    SaveShelveCache('atp', r)
#    SaveShelveCache('test', 'testetessdafsd**********')
    html = GetShelveCache('atp')    
    soup = bs4.BeautifulSoup(html, 'html5lib')
   
#    links = soup.find_all('a', class_='slide')
#    for link in links:
#        print(link['href'])
#        item = link.find('p')
#        print('title',item.get_text())

    tags = soup.find_all('h3', class_='listing-title')    
    for tag in tags:
        link = tag.find('a')
        print(link['href'])
        print(link.get_text())

    
    
if __name__ == '__main__':
    main()
    