# GPS Console application in python using the gps3 library

This program continuosly fetches detailed location data on a user from satellites, such as latitude, longitude, and elevation for display.  
It was written to be run on a Rasberry Pi running the Raspbian OS, but should work on other unix installations that supports gps3. 

#### Disclaimer:
	As it is a GPS application, it needs a USB GPS Receiver to work. 

How to run
----------
Please refer to the user manual PDF included in the docs folder for details. The program gpsd needs to run in the background alongside this application for it to properly interface with the GPS receiver. Brief steps to set this up are included in the user manual. 

Although this is a python project, the requirements at the time asked for a raspbian executable. As such, an executable with the python interpreter is included, and only runs on raspbian.
