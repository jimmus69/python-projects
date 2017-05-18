#! /usr/bin/python
# simpleDatabaseAccess.py

import MySQLdb
import sys

try:
	db = MySQLdb.connect( host='localhost', user='sherlock',
						  passwd='holmes', db='classicmodels' )

	cursor = db.cursor()

	cursor.execute('select contactLastName, country, city from customers')

	numberRows = int(cursor.rowcount)

	for x in range(0, numberRows):
		row = cursor.fetchone()
		print "%20s, %-20s" % (row[2], row[1])

except db.Error, e:
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)
