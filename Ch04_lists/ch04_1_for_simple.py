#! /usr/bin/env python

"""
     Program: ch04_1.py

    Function:  Explor the for command

"""

p = "Plum Lucky!"

for i in p:
    print i.upper()
    if i == 'u': break
else:
    print "That's all folks!"

print "i = ", i


