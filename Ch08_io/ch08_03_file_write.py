#! /usr/bin/python

"""
     Program: ch08_02_file_write.py
    Function: An exploration of simple conversion
"""
from __future__ import print_function
import os

integer_variable = 34567890123456
print("integer:", integer_variable)

float_variable = 3.14596265358979323
print("  float:", float_variable)

string_variable = "This is a relatively short string"
print(" string:", string_variable)

try:
    file_working = open( "output.txt", "w" )
except:
    print( "Could not open output.txt for write", file=os.stderr)
    exit(1)

file_working.write( str(integer_variable) + '\n')
file_working.write( str(float_variable) + '\n')
file_working.write( string_variable + '\n')

file_working.close()

print( "That's all folks!" )
