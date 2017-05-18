#! /usr/bin/env python

"""
     Program:  ch05_05_function_no_return.py
    Function:  Exploring what happens when the function does not end
               with a return
"""

def simple_function():
    print "in simple_function()"
    c = 1 + 4
    return c
#    return

return_value = simple_function()

type_return_value = type(return_value)

print " The type of the return value: ", type_return_value
print "The value of the return value: ", return_value




