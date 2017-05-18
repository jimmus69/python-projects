#! /usr/bin/env python

"""
THIS HAS BEEN MOVED TO TUPLES AND DICTIONARY FOR EXPLANATION
     Program: ch04_6_enumerate.py

    Function:  Explor the for command

"""

j = "Plum Lucky"

for (offset,value) in enumerate(j):
    print "value at", offset, "is", value
else:
    print "That's all folks!"







