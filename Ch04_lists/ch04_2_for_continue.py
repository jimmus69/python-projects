#! /usr/bin/env python

"""
     Program: ch04_2.py

    Function:  Explor the for command

"""

p = "Plum Lucky!"

for i in p:
    if i in 'aieou': continue
    print i.upper()

print "i = ", i
print "That's all folks!"

