#! /usr/bin/env python

"""
     Program:  ch06_01_01_module_import.py
    Function:  An introduction to module use
"""

import first

def simple_function():
    print "The value of mod_int:", first.mod_int

print "Using add_2 from frist to add 5 + 3 = ", first.add_2(5, 3)

print "Accessing mod_int =", first.mod_int
print "Accessing mod_list =", first.mod_list

first.ident()

simple_function()

print "That's all folks!"
