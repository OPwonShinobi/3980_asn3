from datetime import datetime
from gps3 import gps3
"""
Source: gpsprint.py
Contains the print function to this GPSD client.
As such, handles all printing of GPS data. 

However, printing of UI user instructions are handled in gps_utils.py
since they don't print out any gps data.

Functions: printData(gpsData): void
		   decimalToDegMinSec(decimalStr): tuple
		   truncateFloat(wholeFloat): float

Date: Nov 1 2017
Designer: Keir Forster
Programmer: Alex Xia   	
"""

# Function: printData
# Designer: Alex Xia
# Programmer: Keir Forster
# Date: Nov 1 2017
# Argument: gpsData - data parsed from gpsd daemon in json format 
#					  data's format stored in python however is a series
# 					  of nested lists and python dictionaries(maps)
# 
# Formats and prints out json data sent from gps daemon
# Depending on availability of data passed in, format changes.
# 	ie. 4 satellites allow more data to be printed than no satellites 
def printData(gspData):
	try:		
		satellites = gspData.SKY['satellites']
		dateStr = "n/a"
		if isinstance(satellites, list) and len(satellites) > 0:
			dateStr = gspData.GST['time']
			for satellite in gspData.SKY['satellites']:
				prn = int(satellite['PRN'])
				el = int(satellite['el'])
				azi = int(satellite['az'])
				snr = int(satellite['ss'])
				used = satellite['used']
				print("PRN = {:03} Elevation = {:03} Azimuth = {:03} SNR = {:03} Used = {}".format(
					prn, el, azi, snr, used))
		if isinstance(satellites, list) and len(satellites) > 3:	
			lat = gspData.TPV['lat']
			lon = gspData.TPV['lon']
			if lat == "n/a" or lon == "n/a":
				print("{} Latitude: {} Longitude: {}\n".format(dateStr, lat, lon)	)
			else:
				latTuple = decimalToDegMinSec(lat)
				lonTuple = decimalToDegMinSec(lon)
				latDirection = 'N'
				if latTuple[0] < 0:
					latDirection = 'S'
				lonDirection = 'E'
				if lonTuple[0] < 0:
					lonDirection = 'W'
				print("{}\nLatitude: {} Deg, {} Min, {} Sec {}\nLongitude: {} Deg, {} Min, {} Sec {}\n".format(
					dateStr, abs(latTuple[0]), latTuple[1], latTuple[2], latDirection, 
					abs(lonTuple[0]), lonTuple[1], lonTuple[2], lonDirection))
		else:
			print("{} {}\n".format(dateStr, "n/a"))	
	except Exception as e:
		raise e

# Function: decimalToDegMinSec
# Designer: Alex Xia
# Programmer: Keir Forster
# Revision: Nov 6 2017 - moved from gps_util to gps_print due to python 
# 						 circular dependency problem
# Argument: decimalStr - originally a string, turns out this works with
#					  	floats as well
# 
# Converts a longitude or latitude string in the format of "49.250624 W"
# into degrees, minutes, seconds in the format "49 deg 15min 2.2464sec"
# and returns it as a 3-element tuple.
# 		eg. above example would return tuple(49, 15, 2.2464)
def decimalToDegMinSec(decimalStr):
    # delimits using spaces into list of strings, then casts first elem to float
    decimalFloat = float(str(decimalStr).split()[0])
    degreesInt = int(decimalFloat)
    floatPart = truncateFloat(decimalFloat)
    minutesFloat = abs(floatPart * 60)
    minutesInt = int(minutesFloat)
    floatPart = truncateFloat(minutesFloat)
    secondsFloat = floatPart * 60 
    degTuple = (degreesInt, minutesInt, secondsFloat)
    return degTuple

# Function: truncateFloat
# Designer: Alex Xia
# Programmer: Alex Xia
# Revision: Nov 6 2017 - moved from gps_util to gps_print due to python 
# 						 circular dependency problem
# Argument: wholeFloat - must be a float
# 
# Cleanly truncates the float part of a float from a whole
# float without leaving a trail of zeros
# 		eg. wholeFloat=3.14, return 0.14, never 0.1400000
def truncateFloat(wholeFloat):
    intPart = int(wholeFloat)
    floatPartLen = len(str(wholeFloat)) - len(str(intPart))-1
    floatPartWithJunk = wholeFloat - intPart 
    pattern = "." + str(floatPartLen) + "f" # produces ".2f" style sig fig
    floatPartStr = format(floatPartWithJunk, pattern)
    return float(floatPartStr)

