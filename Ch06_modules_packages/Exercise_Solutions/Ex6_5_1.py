#! /usr/bin/python

"""
     Program:  Ex6_5__1.py
    Function:  Based upon the first character of the key program add (+),
               removes (-), looks up (=) the value for the key, or prints (!)
               the dictionary.
"""

import dictionaryRoutines
dictionary = {}

while True:
    input_key = raw_input( "Enter code key or tap <Enter Key> to quit:  " )
    if input_key == "": break

    action = input_key[0]
    key = input_key[1:]

    if action == '+':
        dictionaryRoutines.add_key( key, dictionary )
    elif  action == '-':
        dictionaryRoutines.remove_key( key, dictionary)
    elif action == '=':
        dictionaryRoutines.lookup_key( key, dictionary)
    elif action == '!':
        dictionaryRoutines.print_dictionary(dictionary)
    else:
        print "Key, %s, not understood" % action

print "\nThat's all folks!"
        

    
