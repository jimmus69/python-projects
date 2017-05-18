#! /usr/bin/env python

def findWithin(start, end):
   masterString = "This is a small collection of various tricks and hints that I have stumbled across while programming in Python. Some are trivial, and some are a bit more tricky. Feel free to steal shamelessly from this collection."
   subString = "and"

   return masterString.find(subString, start, end)


rc = findWithin(0, 20)
print "rc: %d" % rc

rc = findWithin(20, 30)
print "rc: %d" % rc

rc = findWithin(0, 200)
print "rc: %d" % rc
