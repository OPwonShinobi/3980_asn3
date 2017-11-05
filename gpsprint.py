from time import gmtime, strftime
from datetime import datetime
from gps3 import gps3

def printData(gspData):
# def print_data(data=0):
	try:		
		#test case, if IDE will complain dead code
		print("SKY:")
		print(gspData.SKY)
		print("TPV:")
		print(gspData.TPV)
		return
		
		satellitesFound = len(gspData.SKY['satellites'])
		#hard code 4 now
		# satellitesFound = gspData;
		# prn = [21, 29, 6, 27]
		# el = [73, 9, 48, 39]
		# azi = [90, 151, 291, 303]
		# snr = [1, 1, 1, 1]
		# used = ["Y", "Y", "Y", "Y"]
		if satellitesFound > 0:
			# for i in gspData.SKY['satellites']:
			for i in range(0,satellitesFound):
				prn = gspData.SKY['satellites'][i]['PRN']
				el = gspData.SKY['satellites'][i]['el']
				azi = gspData.SKY['satellites'][i]['az']
				snr = gspData.SKY['satellites'][i]['ss']
				used = gspData.SKY['satellites'][i]['used']
				print("PRN={:03} Elevation={:03} Azimuth={:03} SNR={:03} Used={}".format(
					prn, el, azi, snr, used)
					# prn[i], el[i], azi[i], snr[i], used[i])
				)
		dateStr = str( datetime.now() )
		if satellitesFound > 3:	
			lat = gspData.TPV['lat']
			# lat = "49.250624 N"
			lon = gspData.TPV['lon'] 
			# lon = "123.003349 W"
			print("{} Latitude: {} Longitude: {}".format(dateStr, lat, lon))
		else:
			print("{} {}".format(dateStr, "n/a"))	
	except Exception as e:
		raise e


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