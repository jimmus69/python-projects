#! /usr/bin/python

class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1
	
	def next(self):
		self.a, self.b = self.b, self.a+self.b
		return self.a

	def __iter__(self):
		return self

# main program

fibs = Fibs()

for f in fibs:
	print f
	if f > 1000: break

print "That's all folks!"
