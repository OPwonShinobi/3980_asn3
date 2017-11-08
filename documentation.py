"""main function comments on its own page"""
gps_utils_py = "file"
"""
Source: gps_utils.py

This is the heart and lungs of this gpsd client.
The GPSD daemon is called via a python interface, gps3, 
On load, program enters a loop, waiting for and checking user input.
If user enters start, program will enter a continuous read mode, and try to call the gspd daemon for
a host and a port (the defaults are host=127.0.0.1, port=2947).

If a connection with a GPS dongle is successful, program enters a loop waiting for and 
printing any satellite data coming in through the gpsd daemon.    

The user can cancel the connection at any time, program returns to user input loop, until
user calls the program to exit.

Functions: 
	startTerminal() : void
	waitForUserInput() : void
	printWelcomePrompt(firstRun=True) : void
	continuousRead() : void

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

Functions: printData(gpsData): void
		   decimalToDegMinSec(decimalStr): tuple
		   truncateFloat(wholeFloat): float

Date: Nov 1 2017
Designer: Keir Forster
Programmer: Alex Xia   	
"""
# Function: start_terminal
# Designer: Alex Xia
# Programmer: Keir Forster
# Date: Nov 1 2017
# 
# Bring program into state which waits for user input
def startTerminal():

# Function: start_terminal
# Designer: Alex Xia
# Programmer: Keir Forster
# Date: Nov 4 2017
# 
# Starts the loop which prompts and checks for user input.
# Then depending on input('start' or 'exit') calls related GPS connection function
def waitForUserInput():

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
# Revision: Nov 6 2017 - used to check for pynput hotkey to terminate read mode.
# 						 pynput module doesn't work properly on pi. Now 
#						 uses ctrl+c (keyboardInterruptException) hack to stop read.
# 						
# After checking for gps device, puts program into continuous read mode.
def continuousRead():
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
	pass

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
	pass		