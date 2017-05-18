#! /usr/bin/python

"""
     Program:  ch10_01_Python_exceptions.py
    Function:  An exploration of acceptions available in Python.
"""

import sys

a = 10
while True:
    try:
        b = int(raw_input( "Enter a number: " ))
        c = a / b
    except ArithmeticError, error_string:
        print "                       error string =", error_string
        
        str_ArithmeticError = str(ArithmeticError)
        print "               str(ArithmeticError) =", str_ArithmeticError

        print "Exception class (sys.exc_info()[0]) =", sys.exc_info()[0]        
        specific_exception = str(sys.exc_info()[0]).split('.')[-1][:-2]
        print "                 Specific exception =", specific_exception
        
        error_message = str(sys.exc_info()[1])
        print "  Error message (sys.exc_info()[1]) =", error_message
 
#        print "\nDATA FROM RAISE\n"
#        raise
    else: 
        print "The value of 10 /", b, "is", c



