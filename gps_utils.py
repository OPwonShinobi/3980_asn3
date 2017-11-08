from gpsprint import printData
from gps3 import gps3
from datetime import datetime
import time
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

# Function: start_terminal
# Designer: Alex Xia
# Programmer: Keir Forster
# Date: Nov 1 2017
# 
# Bring program into state which waits for user input

def startTerminal():
	waitForUserInput():

# Function: start_terminal
# Designer: Alex Xia
# Programmer: Keir Forster
# Date: Nov 4 2017
# 
# Starts the loop which prompts and checks for user input.
# Then depending on input('start' or 'exit') calls related GPS connection function

def waitForUserInput():
	printWelcomePrompt(True)	
	while True:
		try:
			userInput = input(">>> ")
			if userInput.isalpha() and userInput.lower() == "start":
				# this throws exception
				continuousRead()
				# don't print this if exited
			elif userInput.isalpha() and userInput.lower() == "exit":
				return
			else:
				print(">>> Invalid input, please enter 'start' or 'exit'")
			#this ran when input = start, and when no device found (exception raised) 
			printWelcomePrompt(False)	
		except KeyboardInterrupt:
			print("\n")
			printWelcomePrompt(False)	
		except Exception as e: 
			raise e
			print("Warning: " + str(e))
			printWelcomePrompt(False)	

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
    if firstRun:
        print("*{:*<70}*".format("*"))
        print("* {:<69}*".format("A dumb GPS terminal program."))
        print("* {:<69}*".format("Enter 'start' to start reading from your GPS"))
        print("* {:<69}*".format("Enter 'exit' to exit this application"))
        print("* {:<69}*".format("Or, diselect this terminal, and hit 'q' to stop a running connection."))
        print("*{:*<70}*".format("*"))
    else:
        print("*{:*<70}*".format("*"))
        print("* {:<69}*".format("connection ended."))
        print("* {:<69}*".format("Enter 'start' to restart reading from your GPS"))
        print("* {:<69}*".format("Enter 'exit' to exit this application"))
        print("* {:<69}*".format("Or, diselect this terminal, and hit 'q' to stop a running connection."))
        print("*{:*<70}*".format("*"))

# Function: continuousRead
# Designer: Alex Xia
# Programmer: Keir Forster
# Revision: Nov 6 2017 - used to check for pynput hotkey to terminate read mode.
# 						 pynput module doesn't work properly on pi. Now 
#						 uses ctrl+c (keyboardInterruptException) hack to stop read.
# 						
# After checking for gps device, puts program into continuous read mode.
def continuousRead():
	try:			
		# calls constructor of gpsd daemon's interface
		gpsSocket = gps3.GPSDSocket()
		# calls constructor of json data stream adapter
		jsonBuffer = gps3.DataStream()
		# connects to port
		gpsSocket.connect()
		# sets the ?WATCH= json tag to enabled
		gpsSocket.watch()
		# deal with all data coming in from socket
		for incomingData in gpsSocket:
			# valid data
			if incomingData:
				# now jsonBuffer has the json as dict 
				jsonBuffer.unpack(incomingData)
				printData(jsonBuffer)
				time.sleep(0.5)
	except KeyboardInterrupt as e_intentional:
		raise e_intentional
	except Exception as e:
		raise e
