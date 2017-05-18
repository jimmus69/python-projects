#! /usr/bin/python

"""
     Program: ch08_03_02_filter_lambda.py
    Function: An explorataion of the builtin filter
"""

even_numbers = filter(lambda x: not (x % 2), range(10))

print even_numbers
print "That's all folks!"
