#! /usr/bin/python

replaceIn = raw_input( "Enter string to replace in: " )
replaceString = raw_input( "Enter string to replace: " )
replaceWith = raw_input( "Enter replacement string: " )

newString = replaceIn.replace( replaceString, replaceWith )

print "new string:", newString
