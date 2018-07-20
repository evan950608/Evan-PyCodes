# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 16:58:51 2018

@author: evan9
"""

import urllib.request, urllib.parse, urllib.error
import json
import Json_Exer_2_Locs

service_url = 'http://py4e-data.dr-chuck.net/geojson?'
#**** import the locations list ****
locs = Json_Exer_2_Locs.locs_full()

fhand = open(r'c:\PyCodes\File\_temp0.txt', 'w')

for loc in locs:
    address_url = urllib.parse.urlencode({'address': loc})
    url = service_url + address_url
    
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    
    try:
        js = json.loads(data)
    except:
        js = None
        
    #**** Make sure js['status'] is 'OK' ****
    if js == None or 'status' not in js or js['status'] != 'OK':
        print(data)
        print('==== Failure To Retrieve ====')
        continue
    
    #**** Take useful information ****
    latitude = js["results"][0]["geometry"]["location"]["lat"]
    longitude = js["results"][0]["geometry"]["location"]["lng"]
    formatted_address = js["results"][0]["formatted_address"]
    place_id = js["results"][0]["place_id"]
    
    #**** Output Format ****
    output = '''
{0}
    Latitude: {1}
    Longitude: {2}
    Formatted Address: {3}
    Place_ID: {4}
    '''.format(loc, latitude, longitude, formatted_address, place_id)
    print(output)
    
    #**** Error Message ****
    error = '''
{0}
    ==== Unable to Write ====
    '''.format(loc)
    
    try:
        fhand.write(output)
    except:
        fhand.write(error)
        continue
    
#    print(loc)
#    print('   ', 'Latitude:', latitude)
#    print('   ', 'Longitude:', longitude)
#    print('   ', 'Formatted Address:', formatted_address)
#    print('   ', 'Place_ID:', place_id)
#    print('')
    
fhand.close()
input('Press enter to continue...')
    
    
    
    
    
    
    