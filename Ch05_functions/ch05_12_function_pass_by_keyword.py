#! /usr/bin/env python

"""
     Program:  ch05_12_function_pass_position.py
    Function:  Exploring simple pass by position
"""

def simple_function(a, b, c):
    print "I am from simple_function"
    print "The value of a: ", a
    print "The value of b: ", b
    print "The value of c: ", c
    return 

print "\nCalled as simple_function( 10, 'my string', 5)"
simple_function( 10, 'my string', 5)

print "\nThat's all folks!"

