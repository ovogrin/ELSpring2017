import os
import time
import sqlite3 as mydb
import sys

#Logs date time into a testTime database.
#Logs are done in the format of YYYY-MM-DD and HH-MM-SS

def logTime():
	xTime = time.strftime('%Y-%m-%d')
	xDate = time.strftime('%H-%M-%S')
	list1 = [xTime, xDate]

	con = mydb.connect('testTime.db')
	with con:
		try:
			cur = con.cursor()
			sql = "insert into TempData values(?,?)"
			cur.execute('insert into testTime values(?,?)',list1)
			print("Time Logged")
		except:
			print("Error!!")

logTime()
