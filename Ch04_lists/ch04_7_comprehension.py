#! /usr/bin/env python

"""
     Program: ch04_7_comprehension.py
    Function: A comprehension written as a for loop
"""

a = range(1,7)

print 'a =', a

a_10 = [ x + 10 for x in a ]

print 'a_10 =', a_10
print "That's all folks!"

