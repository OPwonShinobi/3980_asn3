from datetime import datetime
from gps3 import gps3

def printData(gspData):
	try:		
		satellites = gspData.SKY['satellites']
		if isinstance(satellites, list) and len(satellites) > 0:
			for satellite in gspData.SKY['satellites']:
				prn = int(satellite['PRN'])
				el = int(satellite['el'])
				azi = int(satellite['az'])
				snr = int(satellite['ss'])
				used = satellite['used']
				print("PRN = {:03} Elevation = {:03} Azimuth = {:03} SNR = {:03} Used = {}".format(
					prn, el, azi, snr, used))
		dateStr = str( datetime.now() )
		if isinstance(satellites, list) and len(satellites) > 3:	
			lat = gspData.TPV['lat']
			lon = gspData.TPV['lon']
			if lat == "n/a" or lon == "n/a":
				print("{} Latitude: {} Longitude: {}".format(dateStr, lat, lon)	)
			else:
				latTuple = decimalToDegMinSec(lat)
				lonTuple = decimalToDegMinSec(lon) 
				print("{}\nLatitude: {} Deg, {} Min, {} Sec, Longitude: {} Deg, {} Min, {} Sec".format(
					dateStr, latTuple[0], latTuple[1], latTuple[2], lonTuple[0], lonTuple[1], lonTuple[2]))
		else:
			print("{} {}".format(dateStr, "n/a"))	
	except Exception as e:
		raise e

# precondition: decimalStr must be in this format: "49.250624 #EVERYTHING AFTER IGNORED"
# or a float or int
def decimalToDegMinSec(decimalStr):
    # delimits using spaces into list of strings, then casts first elem to float
    decimalFloat = float(str(decimalStr).split()[0])
    degreesInt = int(decimalFloat)
    floatPart = truncateFloat(decimalFloat)
    minutesFloat = floatPart * 60 
    minutesInt = int(minutesFloat)
    floatPart = truncateFloat(minutesFloat)
    secondsFloat = floatPart * 60 
    # print("deg:{}, min:{}, sec:{}".format(degreesInt, minutesInt, secondsFloat))
    degTuple = (degreesInt, minutesInt, secondsFloat)
    return degTuple

# eg. pass in eg 3.15, return 0.15, never 0.1500
def truncateFloat(wholeFloat):
    intPart = int(wholeFloat)
    floatPartLen = len(str(wholeFloat)) - len(str(intPart))-1
    floatPartWithJunk = wholeFloat - intPart 
    pattern = "." + str(floatPartLen) + "f" # produces ".2f" style sig fig
    floatPartStr = format(floatPartWithJunk, pattern)
    return float(floatPartStr)

"""
Time stamp (UTC)     : system.time?
o Latitude/Longitude : gspData.TPV['lat'] / TPV['lon']
o PRN 				 : gspData.SKY['satellites']['PRN']
o Elevation			 : gspData.SKY['satellites']['el']
o Azimuth			 : gspData.SKY['satellites']['az']
o SNR				 : gspData.SKY['satellites']['ss']
o Used flag (Y or N) : gspData.SKY['satellites']['used']

gspData.TPV['lat'] 
""" 	