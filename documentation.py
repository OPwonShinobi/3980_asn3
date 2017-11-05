"""main function comments on its own page"""
gps_utils_py = "file"
"""
Source: gps_utils.py

This is the heart and lungs of this gpsd client.
The GPSD daemon is called via a python interface, gps3, 
On execution, program enters a loop, calling and checking user commands.
On user command, program will enter connection mode, and try to call the gspd daemon for
a host and a port (defaults host=‘127.0.0.1’, port=2947).
If a connection with a GPS dongle is successful, program enters a loop waiting for and 
printing any satellite data coming in through the gpsd daemon.    
If the user cancels the connection at any time, program returns to user input loop, until
user calls the program to exit.

Flags in JSON are set, 

Functions: 
	on_press(key) : boolean
	startTerminal() : void
	printWelcomePrompt(firstRun=True) : void
	continuousRead() : void
	handleNoDeviceError : void
Class: gpsDeviceException : inherits Exception	

Date: Nov 1 2017
Designer: Keir Forster
Programmer: Alex Xia   	
"""
gpsprint = "file"
"""
Source: gpsprint.py
Contains the print function to this GPSD client.
As such, handles all printing of GPS data. 

However, printing of UI user instructions are handled in gps_utils.py
since they don't print out any gps data.

Functions: printData(gpsData)

Date: Nov 1 2017
Designer: Keir Forster
Programmer: Alex Xia   	
"""

# Global: globalKillSwitch
# A global variable which controls
# the termination of the main gps read loop ends
globalKillSwitch = False

# Function: on_press
# Designer: Alex Xia
# Programmer: Alex Xia
# Date: Nov 4 2017
# Arguments: key - a key object  
# 
# Called when terminal is deselected and a key is pressed on the keyboard 
# Used to check if 'q' is pressed, if true, set globalKillSwitch to True 
def on_press(key):

# Function: start_terminal
# Designer: Alex Xia
# Programmer: Keir Forster
# Date: Nov 4 2017
# 
# Starts the pseudo-UI in the terminal
# Waits for user input, does input validation. 
# Then depending on input('start' or 'exit') calls related GPS connection function
def startTerminal():

# Function: printWelcomePrompt
# Designer: Alex Xia
# Programmer: Alex Xia
# Date: Nov 4 2017
# Arguments: firstRun - boolean which determines if 
# 			 it's user's first time running application
# 
# Prints pseudo-UI user instructions specific to if user has or hasn't start
# completed a gps connection during life of program.
def printWelcomePrompt(firstRun):

# Function: continuousReadDummy
# Designer: Alex Xia
# Programmer: Alex Xia
# Date: Nov 4 2017
# 
# Dummy read function with dummy data
def continuousReadDummy():
	pass

# Function: continuousRead
# Designer: Alex Xia
# Programmer: Keir Forster
# Date: Nov 1 2017
# 
# After checking for gps device, puts program into continuous read mode.
def continuousRead():
	pass

# Function: continuousRead
# Designer: Alex Xia
# Programmer: Keir Forster
# Date: Nov 1 2017
# 
# Called by continuousRead in case no gps device found
# Stops the gps read loop by turning on globalKillSwitch
def handleNoDeviceError():
	pass

# Class: gpsDeviceException
# Designer: Alex Xia
# Programmer: Alex Xia
# Date: Nov 4 2017
# 
# Class which inherits from python Exception. 
# Its constructor takes a single error message as argument. 
# Meant to be raised when cases such as no gsp devices found occur. 
class gpsDeviceException(Exception):
	pass

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
	pass