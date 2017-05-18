#! /usr/bin/python

"""
     Program: ch08_06_01_generator_expressions.py
    Function: An explorataion of generator expressions
"""

a = ( x for x in range(5) )

for b in a:
    print 'b =', b

for c in a:
    print 'c =', c

print "That's all folks!"
