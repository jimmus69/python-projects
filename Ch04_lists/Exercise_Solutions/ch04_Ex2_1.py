#! /usr/bin/python

"""
     Program:  ch04_Ex2_1.py
    Function:  Print the matrix in reverse
"""

import copy

q = [ [ 1, 2, 3],
      [ 4, 5, 6],
      [ 7, 8, 9] ]

qc = copy.deepcopy(q)

qc_range = range(len(qc))
qc_range.reverse()

for i in qc_range:
    qc[i].reverse()
    print qc[i]

print "q =", q

print "That's all folks!"



