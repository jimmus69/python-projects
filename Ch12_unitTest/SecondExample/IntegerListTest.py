#! /usr/bin/python
"""
Unit test for IntegerList.py

"""

__author__ = "Arthur Messenger (Arthur.Messenger@TrainingByROI.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: Wed Dec  8 23:23:05 PST 2010 $"
__copyright__ = "Copyright (c) 2010 Arthur Messenger"
__license__ = "Python"

from IntegerList import  *
import unittest

class GoodKnownListInput(unittest.TestCase):
	"""Good Input Data"""
	def setUp(self):
		self.knownValues = ( [ 1, 2, 3 ], [ 10, 20 ], [ 12345, 989734, 89] )

	def testGoodImput1(self):
		"""Equal asserted check Test 1"""
		for testList in self.knownValues:
			IntegerListVar = IntegerList( testList )
			self.assertEqual(testList, IntegerListVar.iList)

	def testGoodImput2(self):
		"""Equal asserted check Test 2"""
		for testList in self.knownValues:
			IntegerListVar = IntegerList( testList )
			self.assertEqual(testList, IntegerListVar.iList)

class BadKnownListInput(unittest.TestCase):
	"""Bad Input Data"""
	def setUp(self):
		self.knownValues = ( ['b'], [ 10, 'c' ], [ 12345, 'd', 89] )

	def testBadImput(self):
		"""Check error raised if element not integer"""
		for testList in self.knownValues:
			self.assertRaises(NotIntegerError, IntegerList, testList)

if __name__ == "__main__":
	testClasses = [ GoodKnownListInput, BadKnownListInput ]
	for testClass in testClasses:
		temp = str(testClass)
		name = temp.split('.')[-1][0:-2]
		print "Start of test for", name 
		suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
		unittest.TextTestRunner(verbosity=2).run(suite)
		print "End of test for", name, "\n"
