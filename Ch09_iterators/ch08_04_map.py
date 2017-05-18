#! /usr/bin/python

"""
     Program: ch08_04_map.py
    Function: An explorataion of the builtin map
"""

def simple_function( a, b ):
    c = a + b
    d = a * b
    #return d
    return (a, b, c)

tuple_list = map( simple_function, range(3), range(10,13))

print tuple_list
print "That's all folks!"
