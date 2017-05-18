#! /usr/bin/python

"""
     Program: ch07_04_pickle_write.py
    Function: An exploration of the pickle module
"""

from __future__ import print_function

try:
    import cPickle as pickle
except:
    import pickle
import sys

while True:
	while True:
		try: 
			fileName = raw_input( "Enter file to send pickle to:  " )
		except KeyboardInterrupt, error_string:
			print( "Good-bye\n")
			sys.exit(1)
		except EOFError, error_string:
			print( "Good-bye\n")
			sys.exit(1)
		except:
			print("Enter file name. <Ctrl-C> and <Ctrl-D> will exit")
		else:
			break
	try:
		file_pickle = open( fileName,"wb")
	except:
		print("Could not open " + fileName + " for binary writing", file= sys.stderr)
	else:
		break

int_var = 345678901
float_var = 3.14159
dict_var = { 'a':1, 'b':2, 'c':3 }
list_var = [ 1, 2, 3, 4 ]
complex_object = { 'a':[ {'q':"one", 'r':"two"}, 3, "This is odd"],
                   'b':{ 'l':34, 'm':45},
                   'c':"that's all"}

pickle.dump(int_var, file_pickle, pickle.HIGHEST_PROTOCOL)
pickle.dump(float_var, file_pickle, pickle.HIGHEST_PROTOCOL)
pickle.dump(dict_var, file_pickle, pickle.HIGHEST_PROTOCOL)
pickle.dump(list_var, file_pickle, pickle.HIGHEST_PROTOCOL)
pickle.dump(complex_object, file_pickle, pickle.HIGHEST_PROTOCOL)

file_pickle.flush()
file_pickle.close()

print("That's all folks!")
