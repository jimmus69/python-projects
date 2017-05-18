#! /usr/bin/python

a = [ 'ab', 'abc', 'def', 'rq', 'mn', 'xyz' ]
print "a =", a

c = [ x for x in a if len(x) > 2 ]

print "c =", c
