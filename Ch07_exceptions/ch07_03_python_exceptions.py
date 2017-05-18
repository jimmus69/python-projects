#! /usr/bin/python

"""
  Program:  ch07_03_python_exceptions.py
     Function:  An exploration of exceptions available in Python.
"""

import sys

try:
      fd = open (sys.argv[1], 'r')
except Exception, error_string:
      print ""
#      print "Exception class (sys.exc_info()[0]) =", sys.exc_info()[0]        
#      specific_exception = str(sys.exc_info()[0]).split('.')[-1][:-2]
#      print "                 Specific exception =", specific_exception

#      error_message = str(sys.exc_info()[1])
#      print "  Error message (sys.exc_info()[1]) =", error_message
      print "                       Error string =", error_string
      print "\n"
#else: 
line = fd.readline()
while line: 
    print line,
    line = fd.readline()

print "\nThat's All Folks!"

