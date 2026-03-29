#!/usr/bin/python3

import sys
import urllib.request
import json
from nominatim import getCoord
from Umlaute import str2Wstr

OPENSTREATMAP_URL = "https://nominatim.openstreetmap.org"  # constants for the URLs
OPENMETEO_URL = "https://api.open-meteo.com"

tpr = 0
# print(sys.argv)
if len(sys.argv) > 1:
    cities = sys.argv[1:]
else:
    cities = ['Stuttgart', 'Gärtringen', 'München', 'Mössingen', 'Gießen', 'Überlingen']

print('{:12s} {:16s} {:12s} {:12s} {:12s}'.format('Stadt', 'Zeit', 'Temperatur', 'Windgeschw.', 'Richtung'))

# cities = ['Stuttgart', 'Hamburg']
# print(cities)

for city in cities:
    # print(city)
    # https://www.andre-jochim.de/url-encode.htm
    newCity = str2Wstr(city)
    oldCity = city.replace('ä', '%C3%A4').replace('ü', '%C3%BC').replace('ß', '%C3%9F').replace('ö', '%C3%B6')
    coords = getCoord(newCity, tpr=tpr)

    # print('####', coords)

    try:
        lat = coords['lat']
        lon = coords['lon']
    except Exception as ex:
        print(ex)
        print('could not find coord for', city)
        next

    url_we = OPENMETEO_URL+'/v1/forecast?latitude='+lat+'&longitude='+lon+'&current_weather=true'

    with urllib.request.urlopen(url_we) as response:
        data = str(response.read().decode('utf-8'))

    jsond = json.loads(data)

    current_weather = jsond['current_weather']

    time = current_weather['time']
    temperature = current_weather['temperature']
    windspeed = current_weather['windspeed']
    winddirection = current_weather['winddirection']

    print('{:12s} {:16s} {:8.1f} {:10.1f} {:12.0f}'.format(city, time, temperature, windspeed, winddirection))
