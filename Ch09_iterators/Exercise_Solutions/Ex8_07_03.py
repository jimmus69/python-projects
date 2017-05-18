#! /usr/bin/python

"""
     Program: Ex08_1.py
    Function: An explorataion of function generator
"""

def getstring3(listA):
    for string in listA:
        if len(string) > 2:
            yield (string)
        
        

stringList = [ 'ab', 'abc', 'def', 'rq', 'mn', 'xyz' ]
a = getstring3(stringList)

for string3 in a:
    print string3
    
print "That's all folks!"
