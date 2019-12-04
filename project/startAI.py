import re
import json

jsn = json.dumps({'extent': 4096,
 'version': 2,
 'features': [{'geometry': {'type': 'LineString',
    'coordinates': [[2372, 3178],
     [2340, 3152],
     [2328, 3140],
     [2246, 2916],
     [2218, 2816],
     [2204, 2754],
     [2194, 2610],
     [2194, 2528],
     [2202, 2410],
     [2224, 2228],
     [2260, 2004]]},
   'properties': {'road_type': 'Secondary road',
    'traffic_level': 0.4129999876022339,
    'traffic_road_coverage': 'full'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'MultiLineString',
    'coordinates': [[[2234, 2128],
      [2240, 2126],
      [2124, 2124],
      [2036, 2112],
      [1016, 2012],
      [840, 1990],
      [-406, 1858],
      [-410, 1857]],
     [[2260, 2004],
      [2292, 1672],
      [2304, 1600],
      [2316, 1550],
      [2346, 1456],
      [2382, 1362],
      [2504, 1096],
      [2556, 962],
      [2580, 878],
      [2594, 776],
      [2674, -50],
      [2718, -410]]]},
   'properties': {'road_type': 'Secondary road',
    'traffic_level': 0.4309999942779541,
    'traffic_road_coverage': 'full'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[2308, 2116],
     [2272, 2468],
     [2268, 2516],
     [2262, 2576],
     [2256, 2692],
     [2262, 2772],
     [2268, 2810],
     [2276, 2840],
     [2312, 2930],
     [2376, 3102],
     [2378, 3128],
     [2372, 3178]]},
   'properties': {'road_type': 'Secondary road',
    'traffic_level': 0.44699999690055847,
    'traffic_road_coverage': 'full'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[4506, 991],
     [4312, 1092],
     [4090, 1210],
     [3994, 1258],
     [3320, 1606],
     [2944, 1792],
     [2876, 1832],
     [2638, 1964],
     [2482, 2042],
     [2384, 2090],
     [2308, 2116],
     [2240, 2126]]},
   'properties': {'road_type': 'Secondary road',
    'traffic_level': 0.5479999780654907,
    'traffic_road_coverage': 'full'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[1024, 1916],
     [1544, 1970],
     [1898, 1994],
     [2040, 2002],
     [2164, 2006],
     [2260, 2004],
     [2326, 1984]]},
   'properties': {'road_type': 'Secondary road',
    'traffic_level': 0.6050000190734863,
    'traffic_road_coverage': 'full'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[2786, -410],
     [2744, -2],
     [2686, 540],
     [2664, 780],
     [2644, 914],
     [2556, 1144],
     [2476, 1330],
     [2390, 1554],
     [2368, 1640],
     [2358, 1696],
     [2338, 1858],
     [2326, 1984],
     [2308, 2116]]},
   'properties': {'road_type': 'Secondary road',
    'traffic_level': 0.6309999823570251,
    'traffic_road_coverage': 'full'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'MultiLineString',
    'coordinates': [[[-410, 1770],
      [-394, 1772],
      [290, 1852],
      [626, 1878],
      [1024, 1916]],
     [[2326, 1984],
      [2412, 1958],
      [2540, 1896],
      [2962, 1674],
      [3334, 1478],
      [4092, 1092],
      [4430, 912],
      [4506, 869]]]},
   'properties': {'road_type': 'Secondary road',
    'traffic_level': 1.0,
    'traffic_road_coverage': 'full'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'MultiLineString',
    'coordinates': [[[2606, 3870], [2608, 3862], [2538, 3578]],
     [[2432, 3306], [2406, 3242], [2372, 3178]]]},
   'properties': {'road_type': 'Secondary road',
    'traffic_level': 0.4129999876022339,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'MultiLineString',
    'coordinates': [[[2372, 3178], [2406, 3242], [2432, 3306]],
     [[2538, 3578], [2608, 3862], [2606, 3870]]]},
   'properties': {'road_type': 'Secondary road',
    'traffic_level': 0.44699999690055847,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[2102, 4506],
     [2478, 4020],
     [2536, 3950],
     [2598, 3886],
     [2606, 3870]]},
   'properties': {'road_type': 'Secondary road',
    'traffic_level': 0.6629999876022339,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[2606, 3870],
     [2598, 3886],
     [2536, 3950],
     [2478, 4020],
     [2102, 4506]]},
   'properties': {'road_type': 'Secondary road',
    'traffic_level': 1.0,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[2538, 3578], [2492, 3454], [2432, 3306]]},
   'properties': {'road_type': 'Secondary road',
    'traffic_level': 0.4129999876022339,
    'traffic_road_coverage': 'one_side',
    'travel_mode': 'bridge'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[2432, 3306], [2492, 3454], [2538, 3578]]},
   'properties': {'road_type': 'Secondary road',
    'traffic_level': 0.44699999690055847,
    'traffic_road_coverage': 'one_side',
    'travel_mode': 'bridge'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[3244, 4506],
     [2824, 3966],
     [2800, 3938],
     [2760, 3906],
     [2718, 3880],
     [2680, 3874],
     [2650, 3874],
     [2606, 3870]]},
   'properties': {'road_type': 'Connecting road',
    'traffic_level': 0.33899998664855957,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[2606, 3870],
     [2650, 3874],
     [2680, 3874],
     [2718, 3880],
     [2760, 3906],
     [2800, 3938],
     [2824, 3966],
     [3244, 4506]]},
   'properties': {'road_type': 'Connecting road',
    'traffic_level': 0.609000027179718,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[840, 1990],
     [856, 1824],
     [872, 1692],
     [992, 396],
     [1062, -318],
     [1070, -410]]},
   'properties': {'road_type': 'Major local road',
    'traffic_level': 0.7289999723434448,
    'traffic_road_coverage': 'full'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[1237, -410],
     [1228, -286],
     [1154, 578],
     [1090, 1202],
     [1066, 1470],
     [1042, 1720],
     [1016, 2012]]},
   'properties': {'road_type': 'Major local road',
    'traffic_level': 1.0,
    'traffic_road_coverage': 'full'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[4050, 1784], [4506, 1828]]},
   'properties': {'road_type': 'Local road',
    'traffic_level': 0.4480000138282776,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[2773, 4506], [2614, 3924], [2606, 3870]]},
   'properties': {'road_type': 'Local road',
    'traffic_level': 0.6330000162124634,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[4092, 1092], [4090, 1210]]},
   'properties': {'road_type': 'Local road',
    'traffic_level': 0.656000018119812,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'MultiLineString',
    'coordinates': [[[4200, -410], [4198, -380], [4124, 682], [4092, 1092]],
     [[4092, 1092], [4156, 232], [4198, -380], [4200, -410]]]},
   'properties': {'road_type': 'Local road',
    'traffic_level': 0.6710000038146973,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[2606, 3870], [2614, 3924], [2773, 4506]]},
   'properties': {'road_type': 'Local road',
    'traffic_level': 0.6919999718666077,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'MultiLineString',
    'coordinates': [[[4090, 1210], [4092, 1092]],
     [[4506, 1828], [4050, 1784]]]},
   'properties': {'road_type': 'Local road',
    'traffic_level': 0.7360000014305115,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'MultiLineString',
    'coordinates': [[[4506, 2600],
      [4306, 2728],
      [4188, 2810],
      [4048, 2892],
      [4002, 2912],
      [3802, 2976],
      [3410, 3110],
      [3330, 3118],
      [2832, 3120],
      [2632, 3104],
      [2524, 3102],
      [2442, 3114],
      [2420, 3126],
      [2410, 3138],
      [2404, 3148],
      [2382, 3196]],
     [[2382, 3196],
      [2410, 3138],
      [2420, 3126],
      [2442, 3114],
      [2524, 3102],
      [2632, 3104],
      [2832, 3120],
      [3330, 3118],
      [3410, 3110],
      [3924, 2936],
      [4002, 2912],
      [4048, 2892],
      [4188, 2810],
      [4306, 2728],
      [4506, 2600]]]},
   'properties': {'road_type': 'Local road',
    'traffic_level': 0.7519999742507935,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'MultiLineString',
    'coordinates': [[[4090, 1210], [4050, 1784]],
     [[4050, 1784], [4090, 1210]]]},
   'properties': {'road_type': 'Local road',
    'traffic_level': 1.0,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[2562, 3670],
     [2446, 3686],
     [2152, 3752],
     [2084, 3772],
     [1980, 3816],
     [1926, 3848],
     [1844, 3902],
     [1810, 3926],
     [1758, 3978],
     [1722, 4048],
     [1670, 4164],
     [1574, 4428],
     [1552, 4506]]},
   'properties': {'road_type': 'Minor local road',
    'traffic_level': 0.753000020980835,
    'traffic_road_coverage': 'full'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'MultiLineString',
    'coordinates': [[[2884, 1716],
      [2858, 1680],
      [2836, 1628],
      [2774, 1310],
      [2738, 1112],
      [2704, 978],
      [2684, 946],
      [2644, 914],
      [2580, 878]],
     [[3392, 404],
      [3434, 414],
      [3480, 436],
      [3510, 456],
      [3532, 476],
      [3556, 512],
      [3568, 544],
      [3574, 570],
      [3572, 634],
      [3568, 672],
      [3556, 708],
      [3542, 732],
      [3526, 754],
      [3502, 774],
      [3452, 800],
      [3402, 814],
      [3358, 814],
      [3322, 810],
      [3292, 798],
      [3256, 780],
      [3224, 760],
      [3196, 740],
      [3168, 708],
      [3130, 654],
      [3120, 614],
      [3116, 580],
      [3124, 536],
      [3132, 512],
      [3152, 486],
      [3186, 458],
      [3222, 438],
      [3270, 418],
      [3316, 410],
      [3392, 404]]]},
   'properties': {'road_type': 'Minor local road',
    'traffic_level': 1.0,
    'traffic_road_coverage': 'full'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[2686, 540], [2616, 536]]},
   'properties': {'road_type': 'Minor local road',
    'traffic_level': 0.1940000057220459,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'MultiLineString',
    'coordinates': [[[2944, 1792], [2884, 1716]],
     [[3320, 1606],
      [3336, 1644],
      [3368, 1688],
      [3398, 1712],
      [3458, 1726],
      [4050, 1784]]]},
   'properties': {'road_type': 'Minor local road',
    'traffic_level': 0.4480000138282776,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[3272, 1510], [3320, 1606]]},
   'properties': {'road_type': 'Minor local road',
    'traffic_level': 0.47699999809265137,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[2884, 1716], [2944, 1792]]},
   'properties': {'road_type': 'Minor local road',
    'traffic_level': 0.5640000104904175,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'MultiLineString',
    'coordinates': [[[2686, 540], [3116, 580]],
     [[4050, 1784],
      [3458, 1726],
      [3398, 1712],
      [3368, 1688],
      [3336, 1644],
      [3320, 1606]]]},
   'properties': {'road_type': 'Minor local road',
    'traffic_level': 0.7360000014305115,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[2616, 536],
     [1886, 464],
     [1796, 458],
     [1170, 404],
     [992, 396]]},
   'properties': {'road_type': 'Minor local road',
    'traffic_level': 0.7860000133514404,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'LineString',
    'coordinates': [[3246, 3118],
     [3218, 2586],
     [3210, 2506],
     [3194, 2446],
     [3010, 1950],
     [2944, 1792]]},
   'properties': {'road_type': 'Minor local road',
    'traffic_level': 0.800000011920929,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2},
  {'geometry': {'type': 'MultiLineString',
    'coordinates': [[[992, 396],
      [1170, 404],
      [1796, 458],
      [1886, 464],
      [2616, 536],
      [2686, 540]],
     [[3116, 580], [2686, 540]],
     [[2944, 1792],
      [3010, 1950],
      [3194, 2446],
      [3210, 2506],
      [3218, 2586],
      [3246, 3118]],
     [[3320, 1606], [3272, 1510], [3270, 1470], [3272, 1422], [3322, 810]],
     [[3476, -410], [3462, -300], [3392, 404]],
     [[3322, 810], [3272, 1422], [3270, 1470], [3272, 1510]],
     [[3392, 404], [3462, -300], [3476, -410]],
     [[4050, 1784],
      [4048, 1956],
      [4038, 2052],
      [4032, 2076],
      [4028, 2114],
      [4016, 2146],
      [4006, 2166],
      [3990, 2190],
      [3970, 2210],
      [3946, 2230],
      [3910, 2256],
      [3886, 2262],
      [3854, 2280],
      [3210, 2506]],
     [[3210, 2506],
      [3854, 2280],
      [3886, 2262],
      [3910, 2256],
      [3946, 2230],
      [3970, 2210],
      [3990, 2190],
      [4006, 2166],
      [4016, 2146],
      [4028, 2114],
      [4032, 2076],
      [4038, 2052],
      [4048, 1956],
      [4050, 1784]]]},
   'properties': {'road_type': 'Minor local road',
    'traffic_level': 1.0,
    'traffic_road_coverage': 'one_side'},
   'id': 0,
   'type': 2}]}, sort_keys=True)

obj = json.loads(jsn)
print('Before: ' + str(obj))

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

"""extract JSON values without replacement"""
def update_JSONvalues(obj, key):
    """Update all values of specified key from nested JSON."""
    """obj is the JSON, key or k is the key, v is the value"""
    """will only update within the console of use, otherwise return None"""

    def update(obj, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    update(v, key)
                    #print('Searching for Key')
                elif k == key:
                    if v > .75:
                        v = {key:'Best'}
                        obj.update(v)
                        print('Overwriting key value: ' + str(v))
                        return v
                    elif .5 < v <= .75:
                        v = {key:'Good'}
                        obj.update(v)
                        #print('Overwriting key value: ' + str(v))
                        return v
                    elif .25 < v <=.5:
                        v = {key:'OK'}
                        obj.update(v)
                        return v
                    elif 0 <= v <= .25:
                        v = {key:'Avoid'}
                        obj.update(v)
                        return v
                    else:
                        print('pass')
                        pass
                    #arr.append(v)
                    #print(key + str(v))
                
        elif isinstance(obj, list):
            for item in obj:
                update(item, key)
        #return arr
    #print(obj)
    obj = update(obj, key)
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
                    #print('Searching for Key')
                elif k == key:
                    if v > .75:
                        obj[k] = 'Good'
                        obj['pollution_level'] = obj.pop(k)
                        #obj.update(v)
                        return v
                        #print('Overwriting key value: ' + str(v))
                    elif 0 <= v <= .75:
                        obj[k] = 'Avoid'
                        obj['pollution_level'] = obj.pop(k)
                        #obj.update(v)
                        return v
                    else:
                        print('pass')
                        pass
                    #arr.append(v)
                    #print(key + str(v))
                
        elif isinstance(obj, list):
            for item in obj:
                update(item, key)
        #return arr
    #print(obj)
    obj = update(obj, key)
    return obj


key = 'traffic_level'

overwrite_JSONvalues(obj, key)
print(obj)
