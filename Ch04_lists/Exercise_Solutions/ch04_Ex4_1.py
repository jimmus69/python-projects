#! /usr/bin/python

"""
     Program:  ch04_Ex4_1.py
    Function:  Build and access a dictionary
"""

dictionary = {}

while True:
    key_wanted = raw_input( "Enter the key wanted or exit to stop:  " )

    if key_wanted == 'exit':
        break

    if dictionary.has_key(key_wanted):
        print key_wanted, "->", dictionary[key_wanted]
        continue
    else:
        print "Dictionary does not have key."
        value = raw_input( "Enter value or tap Enter key to continue:  " )
        if value == '':
            continue
        else:
            dictionary[key_wanted] = value

print "\n\nThat's all folks!"

