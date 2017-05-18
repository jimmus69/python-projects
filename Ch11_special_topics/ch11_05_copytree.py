#! /usr/bin/python

import sys
import shutil

if ( len( sys.argv ) != 4 ):
	print >> sys.stderr, sys.argv[0], "src dst ingorePatterns"
	exit(1)

try:
	shutil.copytree( sys.argv[1], sys.argv[2], ignore=shutil.ignore_patterns(sys.argv[3]) )
except:
	print >> sys.stderr, "copytree error"
	print >> sys.stderr, "   Exception class: ", str(sys.exc_info()[0]).split('.')[-1][:-2]
	print >> sys.stderr, "Specific Exception: ", sys.exc_info()[1]
	exit(3)
