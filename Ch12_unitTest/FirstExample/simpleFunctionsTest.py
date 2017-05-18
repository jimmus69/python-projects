#! /usr/bin/python
"""
Unit test for divideFunction
"""
import unittest
import simpleFunctions

class TestGooddivideFunction(unittest.TestCase):
	def setUp(self):
		print "\nFrom Good Setup!"
	
	def tearDown(self):
		print "From Good tearDown!"

	def testGoodInput1(self):
		""" Integer divide """
		self.assertEqual(5, simpleFunctions.divideFunction(10,2))

	def testGoodInput2(self):
		""" Float divide """
		self.assertAlmostEqual(3.3333333, simpleFunctions.divideFunction(10.0,3))

if __name__ == "__main__":
	testClasses = [ TestGooddivideFunction ]
	for testClass in testClasses:
		temp = str(testClass)
		name = temp.split('.')[-1][0:-2]
		print "Start of test for", name 
		suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
		unittest.TextTestRunner(verbosity=2).run(suite)
		print "End of test for", name, "\n"
