#! /usr/bin/python

"""
     Program: ch10_02_01_user_exception.py
    Function: An exploration of user exceptions
"""

import sys

class MyErrors(Exception): pass

def get_number():
    number = int(raw_input("Enter a number (10 - 99): "))
    if number < 10 or number > 99:
        raise MyErrors, "Number must be between 10 and 99"
    return number

while True:
    try:
        number = get_number()
        result = 100 / number
    except  MyErrors, error_string:
        print error_string
    except  (KeyboardInterrupt, EOFError):
        break
    except:
        print "specific exception =", str(sys.exc_info()[0]).split('.')[-1][:-2]
        print "error string =", str(sys.exc_info()[1])
    else:
        print "The value is ", result

print "Good bye!"
sys.exit(0)






