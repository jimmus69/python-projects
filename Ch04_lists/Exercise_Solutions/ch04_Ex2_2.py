#! /usr/bin/python

"""
     Program:  ch04_Ex2_2.py
    Function:  Print the matrix in reverse
"""

import copy

q = [ [ 1, 2, 3],
      [ 4, 5, 6],
      [ 7, 8, 9] ]

qc = copy.deepcopy(q)

qc.reverse()


[ qc[i].reverse() for i in range(len(qc)) ]

print "qc =", qc

print "That's all folks!"



