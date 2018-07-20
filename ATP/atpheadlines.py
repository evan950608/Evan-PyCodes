# -*- coding: utf-8 -*-
"""
Created on Sat May 19 11:19:57 2018

@author: Ennio
"""

import urllib
import bs4
import shelve
import os
import sys

def GetWebPage(url):
    #----simple way
    #html = urllib.request.urlopen(url).read() #url = 'http://www.bbc.com/news/uk-politics-44174575'
    #*****simulate browser*****
    req = urllib.request.Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    html =  urllib.request.urlopen(req).read()
    return html
    
def SaveShelveCache(name, value):
    f_shelve = shelve.open('cache')
    f_shelve[name] = value
    f_shelve.close()

def GetShelveCache(name):    
    try:
        f_shelve = shelve.open('cache')
        return f_shelve[name]
    except:
        return None

def GetValidFilename(fname):
    nonvalid_alphabets = [':','\\','/','*','?','"','<','>','|']
    list_alphabet = [s for s in list(fname.strip()) if s not in nonvalid_alphabets]
    return ''.join(list_alphabet)

def SaveBytesToHtmlFile(title , html, sub_path=None):
    if sub_path != None: 
        if not os.path.exists(sub_path): os.mkdir(sub_path)
        fname = os.path.join(sub_path,GetValidFilename(title+'.html'))
    else:
        fname = GetValidFilename(title+'.html')
    with open(fname , 'wb') as f:
        f.write(html)

def SaveStringToHtmlFile(title , html, path=None):
    if path != None: 
        if not os.path.exists(path): os.mkdir(path)
        fname = os.path.join(path,GetValidFilename(title+'.html'))
    else:
        fname = GetValidFilename(title+'.html')
    with open(fname , 'w') as f:
        f.write(html)


def GetATP_News_EachPage(url , title=None):
    #url = 'http://www.atpworldtour.com/en/news/djokovic-nishikori-rome-2018-friday'
    #*** Paser Web Page ****
    html = GetWebPage(url)
    soup = bs4.BeautifulSoup(html, 'html5lib')
    if title == None: title = soup.html.head.title
    print(url)
    div = soup.find('div', id='articleSection').find('div', {'class':'article-copy'})
    for tag in div.find_all('img'): tag.extract()
    for tag in div.find_all('style'): tag.extract()
    for tag in div.find_all('strong'): tag.extract()
    for tag in div.find_all('div', class_='videoWrapper'): 
        src = tag.find('iframe')['src']
        newobj = '<p><a href="{0}" target="_blank">Youtube</a></p>'.format(src)
        tag.replaceWith(bs4.BeautifulSoup(newobj, "html.parser"))
#    for tag in div.findChildren():  tag['class'] = ''

    html = '''
<thml>
    <body bgcolor="LightGrey" style="font-family:Consolas,Georgia;">
        <a href="{0}">
            <h3>{1}</h3>
        </a>
        {2}
    </body>
</thml>'''.format(url, title , div.prettify())
    return html

def GetATP_ResultsPage(url , title=None):
    html = GetWebPage(url)
    #*** Paser Web Page ****
    soup = bs4.BeautifulSoup(html, 'html5lib')
    url_draws = urllib.parse.urljoin(url, soup.find('a', string='Draw')['href'])
    
    table = soup.find('table', class_='day-table')
    for tag in table.find_all('img'): 
        tag['src'] = urllib.parse.urljoin(url, tag['src'])

    html = '''
<thml>
    <head>
        <link rel="stylesheet" href="{3}" />
    </head>
    <body bgcolor="LightGrey" style="font-family:Consolas,Georgia">
        <a href="{0}">
            <h1 style="font-size:36px;">{1}</h1>
        </a>
        {2}
    </body>
</thml>'''.format(url, title, table.prettify(), 'http://www.atpworldtour.com/Assets/atpwt/styles/desktop.css?bust=636610494470000000')
    return html, url_draws

def GetATP_DrawsPage(url , title=None):
    html = GetWebPage(url)
    #*** Paser Web Page ****
    soup = bs4.BeautifulSoup(html, 'html5lib')
    table = soup.find('table', class_='scores-draw-table')
    for tag in table.find_all('img'): 
        tag['src'] = urllib.parse.urljoin(url, tag['src'])
    html = '''
<thml>
    <head>
        <link rel="stylesheet" href="{3}" />
    </head>
    <body bgcolor="LightGrey" style="font-family:Consolas,Georgia">
        <a href="{0}">
            <h1 style="font-size:36px;">{1}</h1>
        </a>
        {2}
    </body>
</thml>'''.format(url, title, table.prettify(), 'http://www.atpworldtour.com/Assets/atpwt/styles/desktop.css?bust=636610494470000000')
    return html


def main():
    #*****ATP News************   
    #*** Load Web Page ****
    url = 'http://www.atpworldtour.com/en'
    html = GetShelveCache('atp')
    if html == None:
        html = GetWebPage(url)
        SaveShelveCache('atp',html)
    SaveBytesToHtmlFile('cache',html)
    
    #*** Paser Web Page ****
    soup = bs4.BeautifulSoup(html, 'html5lib')

    
    links = soup.find_all('a',{'class': {'feature-slide-title','slide'}} , href= lambda href: href and "/news/" in href  )
    for link in links:
        href = urllib.parse.urljoin(url, link['href'])
        if len(link.findChildren()) == 0:
            title = link.get_text()
        else:
            item = link.find('p',{'class':'slide-title'})
            title = item.get_text()
        print('href:',href, 'title:',title)
        page = GetATP_News_EachPage(href,title)
        SaveStringToHtmlFile(title, page, 'Htmls')

    h3s = soup.find_all('h3',{'class': 'listing-title'})
    for h3 in h3s:
        link = h3.find('a', href=lambda href: href and "/news/" in href)
        if link == None: continue
        href = urllib.parse.urljoin(url, link['href'])
        title = link.get_text()
        print('href:',href, 'title:',title)
        page = GetATP_News_EachPage(href,title)
        SaveStringToHtmlFile(title, page, 'Htmls')

    #*****ATP Results************
    url = 'http://www.atpworldtour.com/en/scores/current/results?'
    html, url_draws = GetATP_ResultsPage(url, 'ATP Results')
    SaveStringToHtmlFile('results', html, 'Htmls')
    
    #*****ATP Draws************
    url = url_draws
    print(url)
    html = GetATP_DrawsPage(url, 'ATP Draws')
    SaveStringToHtmlFile('draws', html, 'Htmls')


if __name__ == '__main__':
    main()
    
    

   
    
    
    
