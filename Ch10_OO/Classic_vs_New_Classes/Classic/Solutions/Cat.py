from Animal import Animal

class Cat(Animal):
	"""
	Cat a subclass of Animal. 
	"""
	number_of_cats = 0

	def __init__(self, name, eyecolor):
		"""
		Creates a cat instance
		"""
		Animal.__init__(self,name)
		self.eyecolor = eyecolor
		Cat.number_of_cats = Cat.number_of_cats + 1

	def __del__(self):
		if Cat:
			Cat.number_of_cats = Cat.number_of_cats - 1

	def get_eyecolor(self):
		"""
		returns eys color
		"""
		return self.eyecolor

	def set_eyecolor(self, color):
		"""
		sets cat's eye color
		"""
		self.eyecolor = color

	def talk(self):
		"""
		Cat speaks  (Overrides Animal)
		"""
		print '{0} says, "Meow!"'.format(self.name)

	@classmethod
	def get_cat_count(cls):
		return cls.number_of_cats
	

	@classmethod
	def groupName(cls):
		"""
		Return's the name for a collection (group) of cats
		"""
		return "glaring or clowder"

	def __str__(self):
		"""
		Returns formatted instance 
		"""
		return "Instance of {0} colored cat with name {0}".format(self.color, self.name)


	def __eq__(a, b):
		"""
		Checks equality between two Cat instances

		arguments:
		a: first Cat instance
		b: second Cat instance
		"""
		return a.name == b.name
	
	def __ne__(a, b):
		"""
		Checks inequality between two Cat instances
		If done, must be done explicitly from __eq__

		arguments:
		a: first Cat instance
		b: second Cat instance
		"""
		return a.name != b.name
