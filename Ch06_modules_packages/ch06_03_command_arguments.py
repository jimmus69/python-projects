#! /usr/bin/env python

"""
     Program:  ch06_03_command_arguments.py
    Function:  To show how to access command line arguments from
               inside a script and the module name, __name__ of
               an executing script.
"""

import sys

print "__name__ =", __name__

for i in range(0,len(sys.argv)):
    print "argv[%d] =" % i, sys.argv[i]

print "\nThat's all folks!"                   
