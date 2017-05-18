#! /usr/bin/python

import sys
import shutil

if ( len( sys.argv ) != 3 ):
	print >> sys.stderr, sys.argv[0], "src dst"
	exit(1)

try:
	shutil.copy2( sys.argv[1], sys.argv[2] )
except:
	print >> sys.stderr, "   Exception class: ", str(sys.exc_info()[0]).split('.')[-1][:-2]
	print >> sys.stderr, "Specific Exception: ", sys.exc_info()[1]
	exit(2)
