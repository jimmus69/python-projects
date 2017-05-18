#! /usr/bin/env python

name = raw_input( "What is your name:  " )
print "Hello " + name 
print "There should be no new line if I put a comma there " + name,

from time import sleep
sleep(5)
print ("Good bye %s" % name)
