#! /usr/bin/python
"""
Unit test for divideFunction
"""
import unittest
from PersonClass import PersonClass as PC

class TestPersonClass(unittest.TestCase):
	def setUp(self):
		print "\nFrom Good Setup!"
	
	def tearDown(self):
		print "From Good tearDown!"

	def testCounter(self):
		""" test counter """
		a = PC('sam', "USA")
		self.assertEqual(1, PC.classcall())

	def testEquality(self):
		""" test equality """
		a = PC('sam', "USA")
		b = PC('sam', "USA")
		self.assertTrue(a == b)

if __name__ == "__main__":
	testClasses = [ TestPersonClass ]
	for testClass in testClasses:
		temp = str(testClass)
		name = temp.split('.')[-1][0:-2]
		print "Start of test for", name 
		suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
		unittest.TextTestRunner(verbosity=2).run(suite)
		print "End of test for", name, "\n"
