#! /usr/bin/python

import MySQLdb
import MySQLdb.cursors
import sys

try:
	db = MySQLdb.connect( host='localhost', user='sherlock',
						  passwd='holmes', db='classicmodels')
#						  passwd='holmes', db='classicmodels',
#						  cursorclass=MySQLdb.cursors.DictCursor)

	cursor = db.cursor(MySQLdb.cursors.DictCursor)
#	cursor = db.cursor()

	cursor.execute('select contactLastName, country, city from customers')

	rows = cursor.fetchall()

	description = cursor.description
	print "%20s  %-20s" % (description[2][0], description[1][0])

	for row in rows:
		print "%20s, %-20s" % ( row['city'], row['country'])
	
	cursor.close()
	db.close()


except db.Error, e:
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)

