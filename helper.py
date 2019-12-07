'''this file is only for functioning code for the application. please test code remotely before implementing here.'''
#import numpy as np
import math
import requests
import mapbox_vector_tile
# import jsonify
import json

lat = 50
long = 25
tileSize=256
zoom = 15

def gettrafficFlow(lat, long, tileSize, zoom):
    """translate json coordinates into azure maps pixels and form the JSON command"""

    latitude = lat
    longitude = long
    print("1. The latitude, longitude: {0}, {1}".format(latitude, longitude))

    sinLatitude = math.sin(latitude * math.pi / 180)

    pixelX = ((longitude + 180) / 360) * tileSize * math.pow(2, zoom)
    print('px: ' + str(pixelX))
    pixelY = (0.5 - math.log((1 + sinLatitude) / (1 - sinLatitude)) / (4 * math.pi)) * tileSize * math.pow(2, zoom)
    print('py: ' + str(pixelY))
    mapWidth = tileSize * math.pow(2, zoom)
    mapHeight = mapWidth

    numberOfTilesWide = math.pow(2, zoom)
    numberOfTilesHigh = numberOfTilesWide

    print("2. The mapWidth and numberOfTiles: {0}, {1}".format(mapWidth, numberOfTilesHigh))

    tileX = math.floor(pixelX / tileSize)
    tileY = math.floor(pixelY / tileSize)
    print("3. The tileX and tileY estimated.")

    return tileX, tileY


def tileToCoord(tileX, tileY, tileSize, zoom):
    #tileSize = 256
    #zoom = 15
    #extent = 4096 or extract from the tile as tileLayer["extent"]
    mapWidth =  tileSize * math.pow(2, zoom) # tileLayer["extent"]
    mapHeight = mapWidth
    print('Calculated map dimensions at Zoom {0}: {1} wide, {2} high. Please convert to extent key from Map call'.format(zoom, mapWidth, mapHeight))
    pixelX0 = tileX * tileSize #x0 = double(extent) * double(tileX) -- origin pixel from quadtile
    pixelY0 = tileY * tileSize #y0 = double(extent) * double(tileY)-- origin pixel from quadtile
    print('Start pixels for tile:{0},{1} '.format(pixelX0, pixelY0))
    yc = 200##boxtile coordinate from path
    xc = 100##boxtile coordinate from path
    print('Tile coordinate point: {0},{1} '.format(yc, xc))
    y2 = (180 - (yc + pixelY0)) * 360/ mapWidth
    long = ((xc + pixelX0) * 360) / mapWidth - 180
    ##lat function needs fixed
    lat = 360 / math.pi * math.atan(math.exp(y2 * math.pi / 180)) - 90
    print('Calculated return coordinate point:{0},{1}'.format(lat, long))
    
    return long, lat

def azureJSONmaparser(tileX, tileY, tileSize, zoom):
	"""
	API endpoint
	"""
	print('Tile X:' + str(tileX))
	print('Tile Y:' + str(tileY))
	print('Tile Size' + str(tileSize))
	print('Tile Zoom:' + str(zoom))
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
	print('URL: ' +str(URL))
	out = requests.get(url=URL)
	print(out.content)
	obj = mapbox_vector_tile.decode(out.content)
	print(obj)

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

def zoom1(zoom):
    '''calculate current map zoom value'''
    n = 2.0 ** zoom 
    return n

'''below functions calculations need verified for accuracy'''

def num2deg(x, y):
    '''simultaneously convert from vector tile to long and lat coordinates'''
    n = zoom1(zoom)
    #print('x:{0} y:{1}'.format(x,y))
    x1 = x
    y1 = y
    lon = x1 / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * y1 / n)))
    lat = math.degrees(lat_rad)
    return (lat, lon)

def num2lon(x, zoom):
    '''convert from vector tile to lon coordinates'''
    n = 2.0 ** zoom
    lon = x / n * 360.0 - 180.0
    return (lon)

def num2lat(y, zoom):
    '''convert from vector tile to lat coordinates'''
    n = 2.0 ** zoom
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * y / n)))
    lat = math.degrees(lat_rad)
    return (lat)

def tileToCoordJSON(obj, key, zoom):
    """overwrite all values of vector tile coordinates from nested JSON"""
    """into lon and lat. obj is the JSON, key or k is the key, v is the value"""
    """there is a list of uneven lists that needs addressed in this line of"""
    """code."""

    def update(obj, key, zoom):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                #print('entering for loop:{0}{1}'.format(k,v))
                if isinstance(v, (dict, list, tuple)):
                    update(v, key, zoom)
                    if k == key:
                        '''extract coordinates'''
                        #print('Extraction begins')
                        lst = [v]
                        '''JSON call is variable with 2 known cases created by 2 or 3 brackets '''
                        '''that start JSON query. uneven lists within list'''
                        if str(lst)[0:4] == '[[[[':
                            '''repair here'''
                            #print(lst)
                            #v = [[num2deg(x,y) for (x,y) in v] for v in lst]]
                            #print('New coordinate inserted')
                            pass
                            
                        elif str(lst)[0:3] == '[[[':
                            lst = [[[[num2deg(x,y) for (x,y) in v] for v in lst]]]
                            #print('New coordinate inserted')
                            return lst
                        
                        elif str(lst)[0:2] == '[[':
                            lst = [[[num2deg(x,y) for (x,y) in v] for v in lst]]
                            #print('New coordinate inserted')
                            return lst
                        
                        elif str(lst)[0:1] == '[':
                            lst = [[num2deg(x,y) for (x,y) in v] for v in lst]
                            #print('New coordinate inserted')
                            return lst
                        
                        else:
                            print('new case with' + k + 'list discovered.')
                            v = 'error'
                            return v
                        
                        obj[k] = lst
                else:
                    print(obj)
                    #print('Extraction passed')
                    #pass
                
        elif isinstance(obj, list):
            for item in obj:
                update(item, key, zoom)

    obj = update(obj, key, zoom)
    return obj

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
                        '''clean air compared to other locations'''
                        obj[k] = 1
                        obj['pollution_level'] = obj.pop(k)
                        return v
                        # print('Overwriting key value: ' + str(v))
                    elif 0 <= v <= .75:
                        '''more polluted locations'''
                        obj[k] = 0
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
