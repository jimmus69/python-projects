#! /usr/bin/python
"""
Unit test for simpleFunctions
"""
import unittest
import simpleFunctions

class TestGoodSum(unittest.TestCase):
	def setUp(self):
		print "\nFrom Good Setup!"
	
	def tearDown(self):
		print "From Good tearDown!"

	def testBadInput(self):
		""" bad sum """
		self.assertRaises(simpleFunctions.Not_number, simpleFunctions.sumList, [ 1, 'a', 1])

	def testGoodInput(self):
		""" good sum """
		self.assertEqual(3, simpleFunctions.sumList([1, 1, 1]))


if __name__ == "__main__":
	testClasses = [ TestGoodSum ]
	for testClass in testClasses:
		temp = str(testClass)
		name = temp.split('.')[-1][0:-2]
		print "Start of test for", name 
		suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
		unittest.TextTestRunner(verbosity=2).run(suite)
		print "End of test for", name, "\n"
