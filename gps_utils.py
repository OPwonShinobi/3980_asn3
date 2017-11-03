from gpsprint import printData
from gps3 import gps3

def startTerminal():
	print("{}".format("A dumb GPS terminal program."))
	print("{}".format("Enter 'start' to start reading from your GPS"))
	print("{}".format("Enter 'exit' to exit this application"))
	print("{}".format("Enter 'ctrl+q' at any time to return to this screen"))
	bInputValid = False

	while not bInputValid:
		userInput = input()
		if userInput.isalpha() and userInput.lower() == "start":
			continuousRead()
		elif userInput.isalpha() and userInput.lower() == "exit":
			bInputValid = True	
		else:
			print("Invalid input, please enter 'start' or 'exit'")

def continuousRead():
	# calls constructor of gpsd daemon's interface
	gpsSocket = gps3.GPSDSocket()
	# calls constructor of json data stream adapter
	jsonBuffer = gps3.DataStream()
	# connects to port
	gpsSocket.connect()
	# sets the ?WATCH= json tag to enabled
	gpsSocket.watch()
	# wait goes here
	updatedData = None
	for updatedData in gpsSocket:
	    if updatedData:
	    	# now data_stream has the json as dict 
	        jsonBuffer.unpack(updatedData)
	printData(updatedData)

def errorCheck():
	print("error_check called")