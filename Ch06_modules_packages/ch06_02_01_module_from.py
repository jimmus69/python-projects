#! /usr/bin/env python
"""
     Program:  ch06_02_01_module_from.py
    Function:  An introduction to module use
"""

from first import add_2, mod_int, mod_list

def simple_function():
    print "The value of mod_int:", mod_int

print "Using add_2 from frist to add 5 + 3 = ", add_2(5, 3)

print "Accessing mod_int =", mod_int
print "Accessing mod_list =", mod_list

#first.ident()

simple_function()

print "That's all folks!"
