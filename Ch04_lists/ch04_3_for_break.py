#! /usr/bin/env python

"""
     Program: ch04_3.py

    Function:  Explor the for command

"""

p = "Plum Lucky!"

for i in p:
    if i in 'aieou': break
    print i.upper()

print "That's all folks!"
print "i = ", i


