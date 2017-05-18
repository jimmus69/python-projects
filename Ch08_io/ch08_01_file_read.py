#! /usr/bin/env python

"""
     Program: ch08_01_file_read.py
    Function: First of several script to explore 
              opening and reading from a file.
"""

import sys

work_file = raw_input( "Enter file to read: " )
if work_file == "":
    print >>sys.stderr, "Could not read from", work_file
    sys.exit(1)

file_read = open( work_file, "r")

for line in file_read:
    line = line[:-1]
    print (line)

file_read.close()

print "That's all folks!" 
sys.exit(0)
