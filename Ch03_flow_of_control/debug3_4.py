#! /usr/bin/python

"""
    program:  debug3-4.py

    function:  Print the value!

"""

b = 4
c = 5

a = int( raw_input( "Enter a number:  " ))

if a == 3:
    if b != 4:
        print "Got a == 3 and b != 4"
else:
    print "Got c = 5"


