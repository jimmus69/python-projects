#! /usr/bin/env python

#num1 = input("Number 1: ")
#num2 = input("Number 2: ")

num1 = float(raw_input("Number 1: "))
num2 = float(raw_input("Number 2: "))
num3 = raw_input("Number 3: ")
print "num3=", num3
print "The sum of", num1, "and", num2, "is", num1 + num2

import sys
sys.stdout.flush()
from time import sleep
sleep(2)
print "That's all, folks!"
