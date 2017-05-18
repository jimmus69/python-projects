#! /usr/bin/env python

"""
     Program:  ch05_07_01_functions_shared_objects.py
    Function:  This is a contrived function but does show how mutable
               and immutable object passing work

Outside add_10
      immutable object value = 10
        mutable object value = [1, 2, 3]
Inside add_10
          immutable object   = 20
      Local mutable object   = [11, 12, 13]
   Caller's mutable object   = [1, 2, 3]
Outside add_10
      immutable object value = 10
        mutable object value = [1, 2, 3]               
"""
def add_10( add_10_immutable, add_10_mutable ):
    add_10_immutable += 10
    print "Inside add_10"
    print "          immutable object   =", add_10_immutable

    add_10_mutable = [x+10 for x in add_10_mutable]

    print "      Local mutable object   =", add_10_mutable
    print "   Caller's mutable object   =", mutable

immutable = 10
mutable = [ 1, 2, 3]

print "Outside add_10"
print "      immutable object value =", immutable
print "        mutable object value =", mutable

add_10( immutable, list(mutable) )

print "Outside add_10"
print "      immutable object value =", immutable
print "        mutable object value =", mutable

