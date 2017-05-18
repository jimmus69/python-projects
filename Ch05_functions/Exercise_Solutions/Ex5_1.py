#! /usr/bin/python

"""
     Program:  Ex5_1.py
    Function:  Based upon the first character of the key program add (+),
               removes (-), looks up (=) the value for the key, or prints (!)
               the dictionary.
"""

def add_key( key, dictionary):
    value = raw_input( "Enter value:  ")
    dictionary[key] = value
    print key, "->", value, "added to dictionary"

def remove_key( key, dictionary ):
    if key in dictionary:
       del dictionary[key]
       print key, "removed from dictionary"
    else:
       print key, "not in dictionary"

def lookup_key( key, dictionary ):
    if key in dictionary:
       print key, "->", dictionary[key]
    else:
       print key, "not in dictionary"

def print_dictionary():
    for key in dictionary.keys():
        print key, "->", dictionary[key]

dictionary = {}

while True:
    input_key = raw_input( "Enter code key or tap <Enter Key> to quit:  " )
    if input_key == "": break

    action = input_key[0]
    key = input_key[1:]

    if action == '+':
        add_key( key, dictionary )
    elif  action == '-':
        remove_key( key, dictionary)
    elif action == '=':
        lookup_key( key, dictionary)
    elif action == '!':
        print_dictionary()
    else:
        print "Key, %s, not understood" % action

print "\nThat's all folks!"
        

    
