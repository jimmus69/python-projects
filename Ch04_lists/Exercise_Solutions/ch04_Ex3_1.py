#! /usr/bin/python

"""
     Program:  ch04_Ex3_1.py
    Function:  Add 10 to each element of the matrix
"""

q = [ [ 1, 2, 3],
      [ 4, 5, 6],
      [ 7, 8, 9] ]

for i in range(len(q)):
    for j in range(len(q[i])):
        q[i][j] = q[i][j] + 10

print "q =", q

print "That's all folks!"



