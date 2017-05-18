from Cat import Cat

class TomCat(Cat):
	def talk(self):
		"""
		To call a method in the superclass when the method is
		overridden in the current class. use 
		super(current_class_name, self).method()
		"""
		super(TomCat, self).talk()
		print "Burp!"

