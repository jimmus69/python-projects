#! /usr/bin/python

"""
     Program: ch08_03_02_filter_lambda.py
    Function: An explorataion of the builtin filter
"""

def even( number ):
    if number % 2 == 0:
        return True
    else:
        return False


even_numbers = filter(even, range(10))

print even_numbers
print "That's all folks!"
