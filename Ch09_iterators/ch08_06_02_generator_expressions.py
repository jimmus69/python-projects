#! /usr/bin/python

"""
     Program: ch08_06_02_generator_expressions.py
    Function: An explorataion of generator expressions
"""

a = ( x for x in range(5) if not (x % 2) )

for b in a:
    print 'b =', b



print "That's all folks!"
