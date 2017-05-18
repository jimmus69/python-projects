#! /usr/bin/python

import re

p = re.compile( r'-')

m = p.sub( "", '--abc' )

print m
