#! /usr/bin/python

"""
     Program: Ex08_1.py
    Function: An explorataion of function generator
"""

def getword(path):
    fin = open(path, 'r')
    line_number =0
    for line in fin:
        line_number += 1
        for word in line.split():
            yield (line_number, word)
        
        

a = getword('lines.txt')

for line_word in a:
    if line_word[1] == 'six':
        a.close()
    print line_word[0], line_word[1]
    
print "That's all folks!"
