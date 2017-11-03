from time import gmtime, strftime
from datetime import datetime
from gps3 import gps3

def printData(dataStream):
# def print_data(data=0):
	#this should be explicit
	#hard code 4 now
	# satellitesFound = len(datastream.SKY['satellites'])
	print("im called")
	satellitesFound = 0;
	lat = "49.250624 N"
	lon = "123.003349 W"
	prn = [21, 29, 6, 27]
	el = [73, 9, 48, 39]
	azi = [90, 151, 291, 303]
	snr = [1, 1, 1, 1]
	used = ["Y", "Y", "Y", "Y"]
	dateStr = str( datetime.now() )
	if satellitesFound > 0:
		# for i in datastream.SKY['satellites']:
		for i in range(0,satellitesFound):
			print("PRN={:03} Elevation={:03} Azimuth={:03} SNR={:03} Used={}".format(
				prn[i], el[i], azi[i], snr[i], used[i])
			)
	if satellitesFound > 3:	
		print("{} Latitude: {} Longitude: {}".format(dateStr, lat, lon))
	else:
		print("{} {}".format(dateStr, "n/a"))	
	# strftime("", gmtime)


"""
Time stamp (UTC)     : system.time?
o Latitude/Longitude : datastream.TPV['lat'] / TPV['lon']
o PRN 				 : datastream.SKY['satellites']['PRN']
o Elevation			 : datastream.SKY['satellites']['el']
o Azimuth			 : datastream.SKY['satellites']['az']
o SNR				 : datastream.SKY['satellites']['ss']
o Used flag (Y or N) : datastream.SKY['satellites']['used']

datastream.TPV['lat'] 
""" 	