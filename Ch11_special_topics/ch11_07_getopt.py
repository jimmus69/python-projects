#! /usr/bin/python

import getopt
import sys


try:
	optionList, arguments = getopt.getopt( sys.argv[1:], 'ab:d', [ "help", "skip" ] )
except getopt.GetoptError, errorMessage:
	print >> sys.stderr, "GetoptError"
	print >> sys.stderr, errorMessage
	exit(1)
except:
	print >> sys.stderr, "getopt error"
	print >> sys.stderr, "   Exception class: ", str(sys.exc_info()[0]).split('.')[-1][:-2]
	print >> sys.stderr, "Specific Exception: ", sys.exc_info()[1]
	exit(2)


for key, value in optionList:
	print key, ": ", value

print arguments

