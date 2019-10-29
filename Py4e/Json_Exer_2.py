# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 16:16:34 2018

@author: evan9
"""

import urllib.request, urllib.parse, urllib.error
import json


service_url = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    #ex: 'Saint-Petersburg Polytechnic Univesity'
    if len(address) < 1:
        print('==== Search Completed ====')
        break
    address_url = urllib.parse.urlencode({'address': address})
    url = service_url + address_url
    print('Retrieving:', url)
    
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    print('Retrieved {0} characters'.format(len(data)))
    
    try:
        js = json.loads(data)
    except:
        js = None
        
    if js == None or 'status' not in js or js['status'] != 'OK':
        print(data)
        print('==== Failure To Retrieve ====')
        continue
    
    latitude = js["results"][0]["geometry"]["location"]["lat"]
    longitude = js["results"][0]["geometry"]["location"]["lng"]
    formatted_address = js["results"][0]["formatted_address"]
    place_id = js["results"][0]["place_id"]
    
    print('   ', 'Latitude:', latitude)
    print('   ', 'Longitude:', longitude)
    print('   ', 'Formatted Address:', formatted_address)
    print('   ', 'Place_ID:', place_id)
    
    
    
    