#! /usr/bin/python

import copy

q = [[1,2,3],[4,5,6],[7,8,9]];

qa = copy.deepcopy(q)

print [ a.reverse() for a in [ qa[i] for i in range(len(qa) - 1, -1, -1)]]
