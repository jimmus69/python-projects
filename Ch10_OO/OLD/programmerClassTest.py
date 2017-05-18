#! /usr/bin/python
"""
Unit test for Programmer Class
"""
import unittest
from ProgrammerClass import Programmer as P

class TestPersonClass(unittest.TestCase):
	def setUp(self):
		print "\nFrom Good Setup!"
	
	def tearDown(self):
		print "From Good tearDown!"

	def testGet(self):
		""" test get """
		a = P('sam', "USA", "Python")
		self.assertEqual("Python", a.get_language())

	def testSet(self):
		""" test Set """
		a = P('sam', "USA", "Python")
		a.set_language("Scala")
		self.assertEqual("Scala",  a.get_language())

if __name__ == "__main__":
	testClasses = [ TestPersonClass ]
	for testClass in testClasses:
		temp = str(testClass)
		name = temp.split('.')[-1][0:-2]
		print "Start of test for", name 
		suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
		unittest.TextTestRunner(verbosity=2).run(suite)
		print "End of test for", name, "\n"
