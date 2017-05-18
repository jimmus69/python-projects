#! /usr/bin/python

import time
import sys

name = raw_input( "Please enter your first Name:  " )
print "Hello", name 
sys.stdout.flush()
time.sleep(5)
print "Good-bye", name 
