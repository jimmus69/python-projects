#! /usr/bin/python

"""
     Program:  ch04_Ex5_1.py
    Function:  Build and access a dictionary with ability to delete
               from dictionary.
"""

dictionary = {}

while True:
    key_wanted = raw_input( "Enter the key wanted or exit to stop:  " )

    if key_wanted == 'exit':
        break
    if key_wanted[0] == '_':
        key_wanted = key_wanted[1:]
        if dictionary.has_key(key_wanted):
            value = dictionary.pop(key_wanted)
            print key_wanted, "->", value, "deleted."
            continue
        else:
            print "Dictionary does not contain", key_wanted
            continue
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

