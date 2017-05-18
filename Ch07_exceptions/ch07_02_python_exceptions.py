#! /usr/bin/python

"""
     Program:  ch07_02_python_exceptions.py
    Function:  An exploration of exceptions available in Python.
"""

import sys

a = 10

while True:
    try:
        b = int(raw_input( "Enter a number: " ))
        c = a /b
    except ValueError, error_string:
        print "error string =", error_string
        print "specific exception =", str(sys.exc_info()[0]).split('.')[-1][:-2]
    except KeyboardInterrupt, error_string:
        print "error string =", error_string            
        print "specific exception =", str(sys.exc_info()[0]).split('.')[-1][:-2]
    except EOFError, error_string:
        print "error string =", error_string
        print "specific exception =", str(sys.exc_info()[0]).split('.')[-1][:-2]
    except ArithmeticError, error_string:
        print "error string =", error_string
        print "specific exception =", str(sys.exc_info()[0]).split('.')[-1][:-2]
    except:
        print "specific exception =", str(sys.exc_info()[0]).split('.')[-1][:-2]
    else: 
        print "The value of 10 divided by", b, "is", c
        sys.exit(0)







