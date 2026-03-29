#!/usr/bin/python3

from nominatim import getCoord

OPENSTREATMAP_URL = "https://nominatim.openstreetmap.org"  # constants for the URLs
OPENMETEO_URL = "https://api.open-meteo.com"


def str2Wstr(instring, tpr=0):
    byteStr = instring.encode('utf-8')
    byteList = list(byteStr)

    if tpr:
        print('--- str2Wstr:', byteStr)
        print(ascii(byteStr))
        print('--- str2Wstr:', byteList)
        print('--- str2Wstr:', end='')

    newStr = ''
    for ch in byteList:
        if tpr:
            print(ch, chr(ch), end=',')
        if ch < 128:
            newStr += chr(ch)
        else:
            newStr += '%'+hex(ch)[2:]

    if tpr:
        print()
    return newStr


# ===========================================================================
# ---- __main__
if __name__ == "__main__":
    tpr = 1

    cities = ['Gärtringen', 'München', 'Mössingen', 'Gießen', 'Überlingen', 'Österreich']

    for city in cities:
        # print(city)
        newCity = str2Wstr(city, tpr=tpr)
        if tpr: print('newCity:', newCity)

        coords = {'lat': '0.0', 'lon': '90.0'}
        coords = getCoord(newCity, tpr=tpr)
        if tpr: print('####', coords)

        try:
            lat = coords['lat']
            lon = coords['lon']
            print(city, newCity, lat, lon)
        except Exception as ex:
            print(ex)
            print('could not find coord for', city)
            next
