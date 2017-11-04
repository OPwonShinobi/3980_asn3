from gpsprint import printData
from gps3 import gps3
from pynput import keyboard
import time

globalKillSwitch = False

def on_press(key):
    print('\n{0}'.format(key.char + " pressed, connection ending..."))
    if key.char == 'q':
        # Stop listener
        global globalKillSwitch
        globalKillSwitch = True
        return False

def startTerminal():
	printWelcomePrompt(1)	
	bContinueRunning = True

	while bContinueRunning:
		# if not userInput:
		try:
			userInput = input(">>> ")
			if userInput.isalpha() and userInput.lower() == "start":
				#start checking keyboard for q key in background
				keyboard.Listener(on_press=on_press).start()
				continuousReadDummy()
				#stop checking keyboard for q key in background 
				keyboard.Listener(on_press=on_press).stop()
				# print new prompt
				printWelcomePrompt(2)
			elif userInput.isalpha() and userInput.lower() == "exit":
				bContinueRunning = False	
			else:
				print(">>> Invalid input, please enter 'start' or 'exit'")
		except Exception as e: 
			print(e)

def printWelcomePrompt(firstRun=1):
    if firstRun == 1:
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
	# calls constructor of gpsd daemon's interface
	gpsSocket = gps3.GPSDSocket()
	# calls constructor of json data stream adapter
	jsonBuffer = gps3.DataStream()
	# connects to port
	gpsSocket.connect()
	# sets the ?WATCH= json tag to enabled
	gpsSocket.watch()
	# wait goes here
	print("pt A")
	# gpsSocket.next(5000)
	# updatedData = None
	for updatedData in gpsSocket:
		print("pt B")
	if updatedData:
		print("pt C")
		# now data_stream has the json as dict 
		jsonBuffer.unpack(updatedData)
		print("pt D")
	print("pt E")		
	printData(updatedData)
	print("pt F")
	return False

def errorCheck():
	print("error_check called")