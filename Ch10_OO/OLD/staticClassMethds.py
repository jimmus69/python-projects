#! /usr/bin/python

class MyClass(object):

	@staticmethod
	def staticMethod():
		print "This is from a static Method!"

	@classmethod
	def classMethod(cls):
		print "This is from the classMethod", cls

MyClass.staticMethod()

MyClass.classMethod()
