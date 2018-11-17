from gps_utils import startTerminal
"""
Source: dcgps.py
This is a terminal gps client for linux OS's, which uses the gpsd daemon and a GPS dongle to find satellites without needing
an internet connection. 

On load, the program will continuously scan and validate input.
If the user enters "start", program will enter a continous read mode, 
continuously printing out data snapshots from the GPS dongle.

At any time, the user can stop the printing by hitting "ctrl+c" in the terminal.
This stops the connection with the dongle, and brings the program back to its starting state;
the user is once again prompted for either a "start" or a "exit".

On receiving user input to exit, the program will terminate.

Functions: main

Date: Nov 1 2017
Designer: Keir Forster
Programmer: Alex Xia   	

"""
def main():
	startTerminal()

# run main
main()