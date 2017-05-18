#! /usr/bin/python

from tempfile import SpooledTemporaryFile
import os
import sys

ab = SpooledTemporaryFile()

print "start"
os.system( '/usr/bin/free' )

i = 0
stop = int(sys.argv[1])
while( i < stop ):
	print >> ab, "This is line ", i
	i += 1
print "After first writes"
os.system( '/usr/bin/free' )

ab.rollover()
print "rollover executed"
os.system( '/usr/bin/free' )

i = 0
stop = int(sys.argv[1])
while( i < stop ):
	print >> ab, "This is line ", i
	i += 1

print "second run in memory"
os.system( '/usr/bin/free' )
