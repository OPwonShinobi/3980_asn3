from gpsprint import printData
from gps3 import gps3
from datetime import datetime
import time

globalKillSwitch = False

def startTerminal():
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

def continuousReadDummy():
	while not globalKillSwitch:
		try:
			satellitesFound = 4
			print("globalKillSwitch: " + str(globalKillSwitch))
			printData(satellitesFound)
			time.sleep(1)
		except KeyboardInterrupt as e:
			print(e)

def continuousRead():
	while not globalKillSwitch:
		try:			
			# calls constructor of gpsd daemon's interface
			gpsSocket = gps3.GPSDSocket()
			# calls constructor of json data stream adapter
			jsonBuffer = gps3.DataStream()
			# connects to port
			gpsSocket.connect()
			# sets the ?WATCH= json tag to enabled
			gpsSocket.watch()
			# gpsSocket.next(1) such a bad idea
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

def handleNoDeviceError():
	global globalKillSwitch
	globalKillSwitch = True
	raise gpsDeviceException("no gps device found")

class gpsDeviceException(Exception):
		"""implementation of the default python exception class, to be raised when
		something is wrong with the device, as noted by desc"""
		def __init__(self, desc):
			self.desc = desc
				