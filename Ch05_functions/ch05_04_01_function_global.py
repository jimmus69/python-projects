#! /usr/bin/env python

"""
     Program:  ch05_04_function_global.py
    Function:  Program for working through global
"""

def outer_function():
    def inner_function():
        global oct
#        print "oct in inner_function =", oct
        oct = 100
        print "oct in inner_function =", oct
        
    oct = 10
    print "oct in outer_function =", oct

    inner_function()

outer_function()

print "  After oct in module =", oct

print "That's all folks!"

