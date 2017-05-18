#! /usr/bin/python

import re

#p = re.compile( r'abc')
p = re.compile( r'xyz')


iterator = p.finditer( '123abc123abc456abc' ) 
found = False
for m in iterator:
	found = True
	print "        The match: ", m.group()
	print "Starting Location: ", m.start()
	print "  Ending location: ", m.end()
	print "   Start and stop: ", m.span()

if ( not found ):
	print "No match found"
