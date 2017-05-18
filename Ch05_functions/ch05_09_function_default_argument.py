#! /usr/bin/env python

"""
     Program:  ch05_09_function_default_argument.py
    Function:  Exploring default values
"""

def simple_function(a, b="A string", c=3.14):
    print "I am from simple_function"
    print "The value of a: ", a
    print "The value of b: ", b
    print "The value of c: ", c
    return 

print "\nCalled as simple_function( 10, 'my string', 344.1)"
simple_function( 10, 'my string',344.1)

print "\nCalled as simple_function( 10, 'my string')"
simple_function( 10, 'my string' )

print "\nThat's all folks!"

