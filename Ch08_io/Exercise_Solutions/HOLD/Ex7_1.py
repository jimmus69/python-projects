#! /usr/bin/python

"""
     Program: Ex7_1.py
    Function: File ch07_01_file_read.py changed to use readlines()
"""

from __future__ import print_function
import sys

work_file = raw_input( "Enter file to read: " )
if work_file == "":
    print("Good bye!", file=sys.stderr)
    exit(1)

try:
    file_read = open( work_file, "r")
except:
    print( "Could not open", work_file, file=sys.stderr)
    exit(1)

lines = file_read.readlines()
file_read.close()

for i in range(0, len(lines)):
    print(lines[i], end="")

print("That's all folks!")
# exit(0)
