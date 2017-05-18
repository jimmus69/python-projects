#! /usr/bin/env python

"""
     Program:  ch05_09_function_tuple_gather.py
    Function:  Exploring default values
"""

def simple_function(a, b = "string", **c):
    print "I am from simple_function"
    print "The value of a: ", a
    print "The value of b: ", b
    print "The value of c: ", c
    return 

print "\nCalled as simple_function( 10, 'my string', d1=5, d2=3, d3=8)"
simple_function( 10, 'my string', d1=5, d2=3, d3=8)

print "\nCalled as simple_function( 10 )"
simple_function( 10 )

print "\nCalled as simple_function(10, b='new vaue', d1=5, d2=3, d3=8)"
simple_function(10, b='new value', d1=5, d2=3,d3=8)

print "\nThat's all folks!"

