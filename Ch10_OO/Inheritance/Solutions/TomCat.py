from Cat import Cat

class TomCat(Cat):
	def talk(self):
		"""
		TomCat talks
		"""

		Cat.talk(self)
		print "Burp!"

