#! /usr/bin/python

import time
import sys

number_one = raw_input( "Enter first number:  ")
number_two = raw_input( "Enter second number: ")

number1 = float( number_one )
number2 = float( number_two )

sum = number1 + number2

print "The sum of", number_one, "and", number_two, "is", sum
sys.stdout.flush()
time.sleep(2)
print "That's all folks!"

