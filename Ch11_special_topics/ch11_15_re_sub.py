#! /usr/bin/python

import re

p = re.compile( r'abc')

m = p.sub( "ABC", '123abc123abc456abc', count = 2 )

print m
