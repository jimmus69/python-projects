#! /usr/bin/python

"""
     Program:  debug5_3.py
    Function:  Sum the values from the dictionary. HINT: values
               There are more than 2 errors
"""

def simple_function( a, *c ):
    if len(c) == 0:
        return False

    for i in range(len(c)):
        a[0] = a[0] + c[i]
    
    return True
    
d = { 'a':1, 'b':2, 'c':3 }
a = [0]

worked = simple_function( a, *d.values() )

if worked:
    print "The the sum is", a[0]
else:
    print "Sum not computed"
