class Animal:
	"""
	Base class for an animal that has a name
	"""

	def __init__(self, name):
		"""
		Defines instance of Animal

		Argument:
		name: name of the animal (string)
		"""
		self.name = name

	def __eq__(self, a):
		return  self.name == a.name

	def __str__(self):
		"""
		What is printed when name of an instance objec is printed
		"""
		return self.name

	def talk(self):
		"""
		Animal speaks
		"""
		print "Generic Animal Sound"

	def get_name(self):
		"""
		Returns animal's name
		"""
		return self.name

	def set_name(self, newName):
		"""
		Sets animal's name

		Arguemnt:
		newName: new name of animal (string)
		"""
		self.name = newName
