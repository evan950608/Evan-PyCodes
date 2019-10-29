# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:44:02 2018

@author: evan9
"""

import urllib.request, urllib.parse, urllib.error
import json

service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    #ex: 'Ann Arbor, MI'
    if len(address) < 1:
        print('==== Search Completed ====')
        break
    
    #*****Encode address to url format*****
    address_url = urllib.parse.urlencode({'address': address})
    #ex: 'address=Ann+Arbor%2C+MI'
    url = service_url + address_url
    print('Retrieving', url)
    
    handle = urllib.request.urlopen(url)
    data = handle.read().decode()
    print('Retrieved {0} characters.'.format(len(data)))
    
    try:
        js = json.loads(data)
    except:
        js = None
    
    #*****Status must be 'OK' to continue*****
    if js == None or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    #*****Print out original json data*****
    print(json.dumps(js, indent=2))
    
    longitude = js['results'][0]['geometry']['location']['lng']
    latitude = js['results'][0]['geometry']['location']['lat']
    location = js['results'][0]['formatted_address']
    
    print('longitude:', longitude)
    print('latitude:', latitude)
    print('location:', location)
    
    
    
    
    
    
    
