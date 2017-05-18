#! /usr/bin/env python
# Program ch4_3_3_for_else.py

#p = "Plum Lucky!"
p = "Plm Lcky!"

for i in p:
    print i.upper()
    if i == 'u': break
else:
    i = "not found"

print "i =", i
