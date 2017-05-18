#! /usr/bin/python

import re

p = re.compile( r'abc')

m = p.split( '123abc123abc456abc' )

print m
