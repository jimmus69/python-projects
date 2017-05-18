#! /usr/bin/python -O

"""
     Program: ch07_06_assertion.py
    Function: An exploration of assertion
"""

import sys

def get_number():
    number = int(raw_input("Enter a number (10 - 99): "))
    assert number > 9 and number < 100, "Number must be between 10 and 99"
    return number

while True:
    try:
        number = get_number()
        result = 100 / number
    except  AssertionError, error_string:
        print error_string
    except  (KeyboardInterrupt, EOFError):
        break
    except:
        print "specific exception =", str(sys.exc_info()[0]).split('.')[-1][:-2]
        print "error string =", str(sys.exc_info()[1])
    else:
        print "The value is ", result

print "Good bye!"
exit(0)







