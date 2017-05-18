#! /usr/bin/python

import re

p = re.compile( r'abc')

# This just returns a list of all matches
m = p.findall( '123abc123abc456abc' )

if ( m ):
	print m
else: 
	print "No match found"
