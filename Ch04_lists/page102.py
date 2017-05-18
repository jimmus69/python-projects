#! /usr/bin/env python

girls = [ 'alice', 'clarice', 'bernice', 'clarice' ]
boys = [ 'chris', 'arnold', 'bob' ]

letterGirls = {}
for girl in girls:
	letterGirls.setdefault(girl[0], [] ).append(girl)
#	letterGirls[girl[0]] = [ girl ]
print letterGirls
print [ b + "+" + g for b in boys for g in letterGirls[b[0]] ]
