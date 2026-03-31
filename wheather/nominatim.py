#!/usr/bin/python3

import urllib.request
import json

OPENSTREATMAP_URL = "https://nominatim.openstreetmap.org"  # constants for the URLs
OPENMETEO_URL = "https://api.open-meteo.com"


def getCoord(city, tpr=0):
    url_ra = OPENSTREATMAP_URL+'/search?q='+city+'&format=json&limit=1'
    # url_ra = 'https://nominatim.openstreetmap.org/status'
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 ' +
           '(KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}

    if tpr:
        print(url_ra)
    # https://stackoverflow.com/questions/24226781/changing-user-agent-in-python-3-for-urrlib-request-urlopen
    req = urllib.request.Request(url_ra, data=None, headers=hdr)

    try:
        response = urllib.request.urlopen(req)
    except Exception as ex:
        print(ex)
        return ex
    else:
        body = str(response.read().decode('utf-8'))

    try:
        coords = {'lat': json.loads(body)[0]['lat'], 'lon': json.loads(body)[0]['lon']}
    except Exception as ex:
        print(ex)
        return ex

    if tpr:
        print(coords)

    return coords


# ===========================================================================
# ---- __main__
if __name__ == "__main__":
    city = 'Stuttgart'
    coords = getCoord(city)
    print(coords)
