"""
	   Class: IntegerList
	    File: IntegerListClass.py
	Function: Explore some more about classes using a list of integers
"""

__author__    = "Arthur Messenger (Arthur.Messenger@TrainingByROI.com)"
__version__   = "$Revision: 1.0 $"
__date__      = "$Date: Wed Dec  8 23:15:54 PST 2010 $"
__copyright__ = "Copyright (c) 2010 Arthur Messenger"
__license__   = "Python"

class IntegerListError(Exception): pass
class NotIntegerError(IntegerListError): pass

class IntegerList:

	def __init__( self, integer_list ):
		"""
		Initialization of IntegerList
		raises error if not passed in a list of integers
		"""
		for i in range( len(integer_list)):
			istr = str(integer_list[i])
			if not istr.isdigit():
				errorMessage = "Location " + str(i) + " not an integer"
				raise NotIntegerError, errorMessage
		self.iList = integer_list

	def reverse( self ):
		self.iList.reverse()
		return self.iList

	def display( self ):
		return str(self.iList)[1:-1]
			
	def __add__(self, value):
		for q in range(len(self.iList)):
			self.iList[q] = self.iList[q] + value
		return self.iList
				
							 
