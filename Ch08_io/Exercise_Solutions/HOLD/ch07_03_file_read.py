#! /usr/bin/python

"""
     Program: ch07_03_file_read.py
    Function: An exploration of simple conversion
"""
from __future__ import print_function
import os

try:
    file_working = open( "output.txt", "r" )
except:
    print( "Could not open output.txt for reading", file=os.stderr)
    exit(1)

integer_string = file_working.readline()
integer_string = integer_string[:-1]
integer_variable = int( integer_string)
print("integer:", integer_variable)

float_string = file_working.readline()
float_string = float_string[:-1]
float_variable = float(float_string)
print("  float:", float_variable)

string_variable = file_working.readline()
print(" string:", string_variable, end="")

file_working.close()

print( "That's all folks!" )
