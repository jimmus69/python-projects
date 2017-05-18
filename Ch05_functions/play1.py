#! /usr/bin/env python

def ab( rq ):
	ra = list(rq)
	for i in range(len(ra)):
		ra[i] += 10;
		print ra[i]


s = [ 1,2,3,4 ]

ab(s);
print s
