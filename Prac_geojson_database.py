# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:57:13 2018

@author: evan9
"""

import urllib.request, urllib.parse, urllib.error
import json
import Json_Exer_2_Locs
import sqlite3

def set_up_database(cur):
    cur.execute('DROP TABLE IF EXISTS Geojson_Write')
    cur.execute('''CREATE TABLE Geojson_Write (
                Location TEXT, 
                Latitude FLOAT, 
                Longitude FLOAT, 
                Formatted_Address TEXT, 
                Place_ID TEXT)''')
    return

def retrieve_json(loc):
    service_url = 'http://py4e-data.dr-chuck.net/geojson?'
    address_url = urllib.parse.urlencode({'address': loc})
    url = service_url + address_url
    
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    
    try:
        js = json.loads(data)
    except:
        js = None
        
    ### Make sure js['status'] is 'OK' ###
    if js == None or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        return None
    
    return js

def get_infomation(js, loc):
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    addr = js["results"][0]["formatted_address"]
    pid = js["results"][0]["place_id"]
    infos = (loc, lat, lng, addr, pid)
    
    return infos

def write_to_database(cur, infos):
    cur.execute('''INSERT INTO Geojson_Write 
                (Location, Latitude, Longitude, Formatted_Address, Place_ID)
                VALUES (?,?,?,?,?)''', infos)
    return

def main():
    conn = sqlite3.connect(r'c:\PyCodes\Database\Evan.sqlite')
    cur = conn.cursor()
    set_up_database(cur)
    locs = Json_Exer_2_Locs.locs_full()
    
    i = 0
    for loc in locs:
        js = retrieve_json(loc)
        if js == None: continue
        infos = get_infomation(js, loc)
        write_to_database(cur, infos)
        i += 1
        ### Commit every 10 iterations ###
        if i % 10 == 0: conn.commit()
        print(infos)
    
    conn.commit()
    cur.close()
    return

        
if __name__ == '__main__':
    main()
    input('Press enter to continue...')
    
        
    
    
    
    
    
    
    
        