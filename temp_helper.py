import numpy as np
import pandas as pd

import osmnx as ox
import networkx as nx

import math
import requests
import mapbox_vector_tile

def pathFinder(A, B):

    location_point = A
    G = ox.graph_from_point(location_point, distance=1000, clean_periphery=False)
    
    origin = A
    destination = B 
    
    origin_node = ox.get_nearest_node(G, origin)
    destination_node = ox.get_nearest_node(G, destination)
    
    route = nx.shortest_path(G, origin_node, destination_node, method='dijkstra')
    fig, ax = ox.plot_graph_route(G, route)
    
    nodes, edges = ox.graph_to_gdfs(G)
    route_df = nodes[nodes.index.isin(route)][["y", "x"]] # latitude, longitude
    
    return route_df

def tileCalculater(latitude, longitude ,tileSize = 512, zoom = 15):
        
    sinLatitude = np.sin(latitude * np.pi/180)
    
    pixelX = ((longitude + 180) / 360) * tileSize * np.power(2, zoom)
    pixelY = (0.5 - np.log((1 + sinLatitude) / (1 - sinLatitude)) / (4 * np.pi)) * tileSize * np.power(2, zoom)
    
    mapWidth = tileSize * np.power(2, zoom)
    mapHeight = mapWidth

    numberOfTilesWide = np.power(2, zoom)
    numberOfTilesHigh = numberOfTilesWide

    tileX = math.floor(pixelX / tileSize)
    tileY = math.floor(pixelY / tileSize)
    
    return tileX, tileY

def extractJsonValues(obj, key):
    
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

def trafficFlow(tileX, tileY, tileSize = 512, zoom = 15):

    """
    API endpoint 
    """

    tileFormat = "pbf"
    style = "relative"
    key = "yf8upXHhjg4n0O5hf-i24-ZKPZN5kRbE4gGT-_3_TOU"

    URL = "https://atlas.microsoft.com/traffic/flow/tile/{0}?api-version=1.0&style={1}&tileSize={2}&zoom={3}&subscription-key={4}&x={5}&y={6}".format(tileFormat,
                                                                                                                                                  style,
                                                                                                                                                  tileSize,
                                                                                                                                                  zoom,
                                                                                                                                                  key,
                                                                                                                                                  tileX,
                                                                                                                                                  tileY) 
    out = requests.get(url=URL)
    tileLayer = mapbox_vector_tile.decode(out.content)
    
    return np.average(extractJsonValues(tileLayer["Traffic flow"], 'traffic_level'))

def main(A, B):

    optimalPath = pathFinder(A, B)
    
    point_to_point_pollution = []
    
    for row in optimalPath.itertuples():
    
        tileX, tileY = tileCalculater(row.y, row.x, tileSize=512, zoom =15)
        normalizedPollution = trafficFlow(tileX, tileY)
        point_to_point_pollution.append(normalizedPollution)
#         print(normalizedPollution)

    print("Path is {0:0.2f}% clean.".format(np.average(point_to_point_pollution)*100))