# import numpy as np
import math
import requests
import mapbox_vector_tile
# import jsonify
import json


def gettrafficFlow(lat, long, tileSize, zoom):
    """translate json coordinates into azure maps pixels and form the JSON command"""

    latitude = lat
    longitude = long
    print("1. The latitude, longitude: {0}, {1}".format(latitude, longitude))

    sinLatitude = math.sin(latitude * math.pi / 180)

    pixelX = ((longitude + 180) / 360) * tileSize * math.pow(2, zoom)
    pixelY = (0.5 - math.log((1 + sinLatitude) / (1 - sinLatitude)) / (4 * math.pi)) * tileSize * math.pow(2, zoom)

    mapWidth = tileSize * math.pow(2, zoom)
    mapHeight = mapWidth

    numberOfTilesWide = math.pow(2, zoom)
    numberOfTilesHigh = numberOfTilesWide

    print("2. The mapWidth and numberOfTiles: {0}, {1}".format(mapWidth, numberOfTilesHigh))

    tileX = math.floor(pixelX / tileSize)
    tileY = math.floor(pixelY / tileSize)
    print("3. The tileX and tileY estimated.")

    return tileX, tileY


def azureJSONmaparser(tileX, tileY, tileSize, zoom):
    """
    API endpoint
    """

    tileFormat = "pbf"
    style = "relative"
    key = "yf8upXHhjg4n0O5hf-i24-ZKPZN5kRbE4gGT-_3_TOU"

    URL = "https://atlas.microsoft.com/traffic/flow/tile/{0}?api-version=1.0&style={1}&tileSize={2}&zoom={3}&subscription-key={4}&x={5}&y={6}".format(
        tileFormat,
        style,
        tileSize,
        zoom,
        key,
        tileX,
        tileY)
    out = requests.get(url=URL)
    tileLayer = mapbox_vector_tile.decode(out.content)
    obj = tileLayer["Traffic flow"]

    return obj


# obj="https://atlas.microsoft.com/traffic/flow/tile/pbf?api-version=1.0&style=relative&tileSize=256&zoom=15&subscription-key=yf8upXHhjg4n0O5hf-i24-ZKPZN5kRbE4gGT-_3_TOU&x=20530&y=10275"

def update_JSONvalues(key, obj):

    """Update all values of specified key from nested JSON. obj is the JSON, key or k is the key, vis the value"""

    # obj = requests.get(url=URL)
    def update(obj, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    update(v, key)
                    print('Searching for Key')
                elif k == key:
                    """reset parameters here to incorporate future air pollution adjustments"""
                    if v > .75:
                        v = {key: 'Best'}
                        obj.update(v)
                        print('Overwriting key value: ' + str(v))
                        return v
                    elif .5 < v <= .75:
                        v = {key: 'Good'}
                        obj.update(v)
                        # print('Overwriting key value: ' + str(v))
                        return v
                    elif .25 < v <= .5:
                        v = {key: 'OK'}
                        obj.update(v)
                        return v
                    elif 0 <= v <= .25:
                        v = {key: 'Avoid'}
                        obj.update(v)
                        return v
                    else:
                        print('Error in JSON')
                        pass
                    # arr.append(v)
                    # print(key + str(v))
        elif isinstance(obj, list):
            for item in obj:
                update(item, key)
                # return arr
                # print(obj)

    returnQuery = update(obj, key)
    return returnQuery


def extract_JSONvalues(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results


def overwrite_JSONvalues(obj, key):
    """Update all values of specified key from nested JSON."""
    """obj is the JSON, key or k is the key, v is the value"""

    def update(obj, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    update(v, key)
                    # print('Searching for Key')
                elif k == key:
                    if v > .75:
                        obj[k] = 'Good'
                        obj['pollution_level'] = obj.pop(k)
                        return v
                        # print('Overwriting key value: ' + str(v))
                    elif 0 <= v <= .75:
                        obj[k] = 'Avoid'
                        obj['pollution_level'] = obj.pop(k)
                        return v
                    else:
                        print('pass')
                        pass

        elif isinstance(obj, list):
            for item in obj:
                update(item, key)

    obj = update(obj, key)
    return obj