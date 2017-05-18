#! /usr/bin/env python

"""
     Program:  ch05_15_function_pass_dictionary.py
    Function:  Exploring key value pairs
"""

def simple_function(a,b ):
    print "I am from simple_function"
    print "The value of a: ", a
    print "The value of b: ", b
    return 

d1 = {'a':1, 'b':3 }
print "\nCalled as simple_function( **d1)"
simple_function( **d1)

print "\nThat's all folks!"

