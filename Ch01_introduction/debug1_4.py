#! /usr/bin/python

# program:  debug4.py
# There is nothing wrong with this program.
# Read about localtime, strftime and print
# out just the time Hours, Minutes, and seconds

from time import localtime, strftime

#print strftime( "%a, %d %b %Y %H:%M:%S", localtime())
print strftime( "%H:%M:%S", localtime())
