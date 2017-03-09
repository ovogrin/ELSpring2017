import os
import time
import sqlite3 as mydb
import sys

# Program to read temperature from a sensor for 10 minutes
# at 30 seconds intervals.  Data is sent to a sqlite database.

# Reads temperature and time.
# Returns the current time, temperature in Fahrenheit, and temperature in Celsius
def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-000006964288/w1_slave")
	tempfile_text = tempfile.read()
	currentTime = time.strftime('%x %X %Z')
	tempfile.close()
	tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF = tempC*9.0/5.0+32.0
	return [currentTime, tempC, tempF]

# Calls readTemp() and logs temperature with time stamp into sqlite db.
def logTemp():
	con = mydb.connect('temperature.db')
	with con:
		try:
			[t,C,F] = readTemp()
			print "Current temperature is: %s F" %F
			cur = con.cursor()
			sql = "insert into temperatureTable values(?,?,?)"
			cur.execute('insert into temperatureTable values(?,?,?)',(t,C,F))
			print "Temperature logged"
		except:
			print "Error!!"

#executes the logTemp() function every 30 seconds for 10 minutes
def logActivity():
	x = 0;
	while(x<20):
		logTemp()
		time.sleep(30)
		x = x + 1

logActivity()
