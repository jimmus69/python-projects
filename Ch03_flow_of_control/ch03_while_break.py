#! /usr/bin/env python

# ch03_while_break.py

sum = 0

while True:
    input_value = raw_input( "Enter next number for sum or \
quit to exit: " )
    if input_value.lower() == "quit": break
    sum = sum + int(input_value)
      
print "Sum = ", sum

