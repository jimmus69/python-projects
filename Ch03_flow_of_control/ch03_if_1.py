#! /usr/bin/env python

# program ch03_if_1.py

a = int(raw_input("First number:  "))
b = int(raw_input("Second number:  "))

if a < b:
    print a, "is less than", b
elif a == b:
    print a, "is equal to", b
else:
    print a, "is greater than", b

print "And that's the truth."
print "Good-bye"



