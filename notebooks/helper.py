###General air quality functions
###AQI functions from http://aqicn.org/map/germany/ or weather stations

from datetime import datetime
import time
import requests
import json

###Queries needed for stationary data sources
def queryAQI():
  """returns the general air quality value from a weather station through AQICN"""
  """please replace Token with one for Team AirFlow"""
	tokenAPI = '5cbc85352d50daca93c5f8a939d9938a5eadaddc'
	coordinates = '49.0069;8.4037'
	requestAQI = 'http://api.waqi.info/feed/geo:' + coordinates + '/?token=' + tokenAPI
	r = requests.get(requestAQI)
	JSON = json.loads(r.text)
	resultAQI = JSON['data']['aqi']

	return resultAQI
  
def queryHC():
  """returns a Current Humidity value from a weather station from Open Maps"""

	URLOpenMaps = 'http://api.openweathermap.org/data/2.5/weather?id=2950159&APPID=72ccdc2901dae2c310d7a7515e005374'
	r = requests.get(URLOpenMaps)
	JSON = json.loads(r.text)
	#city = JSON['name']
	humCurrent= JSON['main']['humidity']
	#tempCurrentRaw = JSON['main']['temp']
	return humCurrent
	
def queryTemp():
  """returns a Current Temperature value from a weather station from Open Maps"""

	URLOpenMaps = 'http://api.openweathermap.org/data/2.5/weather?id=2950159&APPID=72ccdc2901dae2c310d7a7515e005374'
	r = requests.get(URLOpenMaps)
	JSON = json.loads(r.text)
	#city = JSON['name']
	#humCurrent= JSON['main']['humidity']
	tempCurrentRaw = JSON['main']['temp']
	
	return tempCurrentRaw

###functions that translate queries into usable variables
def calcC():
  """converts Open Maps Temperature query into C"""
	tempCurrentRaw = queryTemp()
	tempCurrentC = tempCurrentRaw - 273.15
	return tempCurrentC
	
def calcF():
  """converts Open Maps Temperature query into F"""
	tempCurrentRaw = queryTemp()
	tempCurrentF = (tempCurrentRaw * 1.8) - 459.67
	return tempCurrentF

###functions that return general air quality classifications that are generally accepted. This function is important for the classification of groups an increasing the relevancy of data to the user
def IndexAirQuality():
  """returns one of six states to classify air quality from a weather station listed on AQICN"""
  """this is a large area value of > 5km"""
	resultAQI = queryAQI()
	if resultAQI < 50:
		currentStateAQI = 'Good'
		return currentStateAQI
	elif 51 > resultAQI and resultAQI <= 100:
		currentStateAQI = 'Moderate'
		return currentStateAQI
	elif 101 > resultAQI and resultAQI <= 150:
		currentStateAQI = 'Unhealthy-for-Sensitive-Groups'
		return currentStateAQI
	elif 151 > resultAQI and resultAQI <= 200:
		currentStateAQI = 'Unhealthy'
		return currentStateAQI
	elif 201 > resultAQI and resultAQI <= 300:
		currentStateAQI = 'Very-Unhealthy'
		return currentStateAQI
	else:
		currentStateAQI = 'Hazardous'
		return currentStateAQI

###functions that identify research classified populations and the associated pollutants. Returns only an array of those groups describe in a character string variable.
###currently identified pollutants include: PM2.5, PM10, Black Carbon, Nitris Oxide, Ozone
###future pollutants: sulfur dioxide (SO2)
###suggested future groups: individuals of low status (possibly controversial and imprecise)

def PM10Grouping():
	"""returns an array of demographic groups most at risk with a pollutant PM10"""
	"""Key to code: PM10 <-- pollutant G1, <-- population group #1 """
	"""PM10 is normally associated with diesel immisions or long range transport"""
	"""sources include: https://www.marlborough.govt.nz/environment/air-quality/smoke-and-smog/health-effects-of-pm10"""
	"""https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5551180/"""
	"""PM10 induces asthma attacks and difficulty breathing"""
	PM10G1 = 'Older people with pre-existing conditions'
	PM10G2 = 'Younger people with pre-existing conditions'
	
	return (PM10G1, PM10G2)

def PM25Grouping():
	"""returns an array of demographic groups most at risk with pollutant PM2.5"""
	"""Key to code: PM25 <-- pollutant G1, <-- population group #1 """
	"""sources include https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5551180/"""
	"""PM2.5 is normally associated with the wear of brakes, tires and road surfaces and non-combustion material."""
	"""PM2.5 relates to residential biomass burning (campfires)"""
	PM25G1 = ''
	PM25G2 = ''
	
	return (PM25G1, PM25G2)

def BCGrouping():
	"""returns an array of demographic groups most at risk with pollutant Black Carbon"""
	"""Key to code: BC <-- pollutant G1, <-- population group #1 """
	"""sources include"""
	"""Black Carbon is normally associated with ..."""
	BCG1 = ''
	BCG2 = ''
	
	return (BCG1, BCG2)

def NOxGrouping():
	"""returns an array of demographic groups most at risk with pollutant Nitris Oxides"""
	"""Key to code: NOx <-- pollutant G1, <-- population group #1 """
	"""sources include"""
	"""NOx is normally associated with ..."""
	NOxG1 = ''
	NOxG2 = ''
	
	return (NOxG1, NOxG2)

def O3Grouping():
	"""returns an array of demographic groups most at risk with pollutant Ozone"""
	"""Key to code: O3 <-- pollutant G1, <-- population group #1 """
	"""sources include"""
	"""O3 is normally associated with ..."""
	O3G1 = ''
	O3G2 = ''
	
	return (O3G1, O3G2)
