#import numpy as np
import math
import requests
from mapbox_vector_tile import decode

def gettrafficFlow(lat, long, tileSize, zoom):

	latitude = lat
	longitude = long

	print("1. The latitude, longitude: {0}, {1}".format(latitude,longitude))

	sinLatitude = math.sin(latitude * math.pi/180)

	pixelX = ((longitude + 180) / 360) * tileSize * math.pow(2, zoom)
	pixelY = (0.5 - math.log((1 + sinLatitude) / (1 - sinLatitude)) / (4 * math.pi)) * tileSize * math.pow(2, zoom)

	mapWidth = tileSize * math.pow(2, zoom)
	mapHeight = mapWidth

	numberOfTilesWide = math.pow(2, zoom)
	numberOfTilesHigh = numberOfTilesWide

	print("2. The mapWidth and numberOfTiles: {0}, {1}".format(mapWidth,numberOfTilesHigh))

	tileX = math.floor(pixelX / tileSize)
	tileY = math.floor(pixelY / tileSize)
	print("3. The tileX and tileY estimated.")
	"""
	API endpoint from azure
	"""

	tileFormat = "pbf"
	style = "relative"
	key = "yf8upXHhjg4n0O5hf-i24-ZKPZN5kRbE4gGT-_3_TOU"

	URL = "https://atlas.microsoft.com/traffic/flow/tile/{0}?api-version=1.0&style={1}&tileSize={2}&zoom={3}&subscription-key={4}&x={5}&y={6}".format(tileFormat, style, tileSize, zoom, key, tileX, tileY) 
	return URL

def azureJSONmaparser(URL):
        out = requests.get(url=URL)
        tileLayer = mapbox_vector_tile.decode(out.content)
        trfficData = tileLayer["Traffic flow"]
        return jsonify({trfficData})
