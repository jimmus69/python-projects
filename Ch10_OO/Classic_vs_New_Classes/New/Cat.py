from Animal import Animal

class Cat(Animal):

	def __init__(self, name, eyecolor):
		super(Cat,self).__init__(name)
		self.eyecolor = eyecolor

	def get_eyecolor(self):
		return self.__eyecolor
	def set_eyecolor(self, eyecolor):
		self.__eyecolor = eyecolor
	eyecolor = property(get_eyecolor, set_eyecolor)

	def __str__(self):
		return "My name is " + self.get_name()

	def talk(self):
		"""
		The cat talks!
		"""
		print '{0} says, "Meow!"'.format(self.name)

	@classmethod
	def groupName(cls):
		return "glaring or clowder"
