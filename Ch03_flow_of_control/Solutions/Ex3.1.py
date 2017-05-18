#! /usr/bin/python
# program Ex3.1.py

import sys

while True:
	aIn = raw_input("First number:  ")
	if aIn.isdigit(): break
	if aIn.lower() == 'quit':
		print "Good bye"
		sys.exit( 0 );
	print "You must enter a number or 'quit' to exit"

a = float(aIn)
print a

while True:
	bIn = raw_input("Second number:  ")
	if bIn.isdigit(): break
	if bIn.lower() == 'quit':
		print "Good bye"
		sys.exit( 0 );
	print "You must enter a number or 'quit' to exit"

b = float(bIn)
print b

if    a < b: print a, "is less than", b
elif a == b: print a, "is equal to", b
else:        print a, "is greater than", b




