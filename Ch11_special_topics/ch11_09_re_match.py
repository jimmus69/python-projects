#! /usr/bin/python

import re

p = re.compile( r'abc')

m = p.match( 'abc123abc456abc' )
#m = p.match( '123abc123abc456abc' )

if ( m ):
	print "        The match: ", m.group()
	print "Starting Location: ", m.start()
	print "  Ending location: ", m.end()
	print "   Start and stop: ", m.span()
else: 
	print "No match found"
