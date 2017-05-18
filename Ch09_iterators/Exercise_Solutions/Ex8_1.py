#! /usr/bin/python

"""
     Program: ch08_01_open_iterator.py
    Function: to show how open can be used as an
              iterator in a for loop
"""

for line in open( "Beatrix_Potter_Tales.txt", 'r'):
    print line,

