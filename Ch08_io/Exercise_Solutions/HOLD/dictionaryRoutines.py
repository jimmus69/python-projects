"""
Simple dictionary routines to read and write to a pickle file
"""

def readDictionary( filename ):
	"""
	Read a dictionary from the file 
	and returns it
	"""

	try:
		import cPickle as pickle
	except:
		import pickle
		import sys

	try:
		file_pickle = open( filename, "rb" )
	except:
		return False

	while True:
		try:
			dictionary =  pickle.load(file_pickle)
			file_pickle.close()
			return dictionary
		except:
			file_pickle.close()
			return False

                  
               
def writeDictionary( filename, dictionary):
	"""
	Writes dictionary to new file, filename
	"""

	try:
		import cPickle as pickle
	except:
		import pickle
		import sys

	try:
		file_pickle = open(filename, "wb")
	except:
		return False

	pickle.dump(dictionary, file_pickle, pickle.HIGHEST_PROTOCOL)

	file_pickle.flush()
	file_pickle.close()
	return

def displayDictionary( dictionary ):
	"""
	uses pprint to display the dictionary in a nice format
	"""
	import pprint

	pprint.pprint(dictionary)
	return
