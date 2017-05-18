#! /usr/bin/env python

print "hello!"

while True:
    candidate = raw_input( "Enter number to square or 'quit' to exit:  " )
    if candidate.lower() == 'quit': break
    try:
        number = int(candidate)
    except:
        print "Must enter a number or 'quit' to exit."
        continue
    print number, "squared is", number ** 2

print "That's all folks!"




