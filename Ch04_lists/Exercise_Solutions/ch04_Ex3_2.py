#! /usr/bin/python

"""
     Program:  ch04_Ex3_2.py
    Function:  Add 10 to each element of the matrix
"""

q = [ [ 1, 2, 3],
      [ 4, 5, 6],
      [ 7, 8, 9] ]

q = [ [ q[i][j] + 10 for j in range(len(q[i]))] for i in range(len(q))]

print "q =", q

print "That's all folks!"



