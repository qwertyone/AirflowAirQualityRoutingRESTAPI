import numpy as np
import pandas as pd

import osmnx as ox
import networkx as nx

import math
import requests
import mapbox_vector_tile

def pathFinder(A, B):
    
    route_df = pd.DataFrame()
    
    location_point = A
    G = ox.graph_from_point(location_point, distance=2000, clean_periphery=False)
    
    origin = A
    destination = B 
    
    origin_node = ox.get_nearest_node(G, origin)
    destination_node = ox.get_nearest_node(G, destination)
  
    routes = [p for p in nx.all_shortest_paths(G, origin_node, destination_node)]
    
    for idx, route in enumerate(routes):
    
        nodes, edges = ox.graph_to_gdfs(G)
        routes_stepwise = nodes[nodes.index.isin(route)][["y", "x"]] # latitude, longitude
        routes_stepwise["route"] = idx + 1
        route_df = route_df.append(routes_stepwise)
        
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
    print("URL is: " + str(out))
    tileLayer = mapbox_vector_tile.decode(out.content)
    print("TileLayer is: " + str(tileLayer))
    return np.average(extractJsonValues(tileLayer["Traffic flow"], 'traffic_level'))

def main(A, B):

    optimalPath = pathFinder(A, B)
    suggested_paths_with_pollution_score = {}
    
    for name, group in optimalPath.groupby("route"):
        
        point_to_point_pollution = []
        
        for row in group.itertuples():
            tileX, tileY = tileCalculater(row.y, row.x, tileSize=512, zoom =15)
            normalizedPollution = trafficFlow(tileX, tileY)
            point_to_point_pollution.append(normalizedPollution)
            
        suggested_paths_with_pollution_score[name] = ((group[["x","y"]].values), np.average(point_to_point_pollution)*100)

    return suggested_paths_with_pollution_score
