#! /usr/bin/env python

"""
     Program: ch07_01_file_read.py
    Function: First of several script to explore 
              opening and reading from a file.
"""

import sys

work_file = raw_input( "Enter file to read: " )
if work_file == "":
    print >>sys.stderr, "Could not read from", work_file
    sys.exit(1)

try:
    file_read = open( work_file, "r")
except IOError, err:
    print >> sys.stderr, "Problem with", work_file + "."
    print >> sys.stderr, "IOError: ", err
    sys.exit(1)
except:
    print >>sys.stderr, "Unknow error with" , work_file
    sys.exit(1)


for line in file_read:
    line = line[:-1]
    print (line)

file_read.close()

print "That's all folks!" 
sys.exit(0)
