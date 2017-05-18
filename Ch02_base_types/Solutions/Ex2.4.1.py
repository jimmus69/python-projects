#! /usr/bin/python

searchIn = raw_input( "Enter string to seach in: " )
startAtIn = raw_input( "Enter starting location of seach:  " )
searchFor = raw_input( "Enter string to seacrh for: " )

startAt = int(startAtIn)

foundAt = searchIn.find( searchFor, startAt );

print 'Found "' + searchFor + '"', 'at', foundAt
