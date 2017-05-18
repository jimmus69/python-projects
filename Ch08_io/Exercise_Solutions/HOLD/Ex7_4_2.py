#! /usr/bin/python

import dictionaryRoutines as dr

pickle_in = raw_input("Name of pickle file:  ")

dictionary = dr.readDictionary(pickle_in)

if not dictionary:
   dictionary = {}

while True:
	key = raw_input("Enter key or <enter> to stop input: ")
	if not key:
		break
	value = raw_input("Enter value or <enter> to stop input: ")
	if not value:
		break
	dictionary[key] = value

pickle_out = raw_input("Name of pickle file: ")
dr.writeDictionary(pickle_out, dictionary)

