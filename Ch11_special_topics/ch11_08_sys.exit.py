#! /usr/bin/python 

import sys

try:
	print "from try"
	raise
except:
	print "from except"
	sys.exit("This is from sys.exit")
finally:
	print "From finally"

