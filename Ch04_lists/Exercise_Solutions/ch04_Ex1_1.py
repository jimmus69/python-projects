#! /usr/bin/python

"""
     Program:  ch04_Ex1_1.py
    Function:  Print the diagonal of a matrix
"""

q = [ [ 1, 2, 3],
      [ 4, 5, 6],
      [ 7, 8, 9] ]

d = []

for i in range(len(q)):
    d.append(q[i][i])

print "diagonal =", d
print "That's all folks!"

