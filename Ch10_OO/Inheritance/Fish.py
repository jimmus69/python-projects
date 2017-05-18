from Animal import Animal

class Fish(Animal):
	"""
	Fish is a subclass of Animal. 
	"""
	number_of_fish = 0

	def __init__(self, name, sound):
		"""
		Creates a fish instance
		"""
		Animal.__init__(self,name)
		self.sound = sound
		Fish.number_of_fish = Fish.number_of_fish + 1

	def __del__(self):
		if Fish:
			Fish.number_of_fish = Fish.number_of_fish - 1

	def getName(self):
		"""
		returns fish's name
		"""
		return self.name
	
	def getSound(self):
		"""
		returns sound the fish makes
		"""
		return self.sound

	def setSound(self, sound):
		"""
		sets fish's sound
		"""
		self.sound = sound

	def talk(self):
		"""
		Fish speaks  (Overrides Animal)
		"""
		print '{0} says, {1}'.format(self.name, self.sound)

	@classmethod
	def getFishCount(cls):
		return cls.number_of_fish
	

	@classmethod
	def groupName(cls):
		"""
		Return's the name for a collection (group) of fish
		"""
		return "school of fish"

	def __str__(self):
		"""
		Returns formatted instance 
		"""
		return "Instance of {0} sounded fish with name {1}".format(self.sound, self.name)


	def __eq__(a, b):
		"""
		Checks equality between two Fish instances
		Note: I used a where traditionally I would have used self

		arguments:
		a: first Fish instance
		b: second Fish instance
		"""
		return a.name == b.name and a.sound == b.sound
	
	def __ne__(a, b):
		"""
		Checks inequality between two Fish instances
		If done, must be done explicitly from __eq__

		arguments:
		a: first Fish instance
		b: second Fish instance
		"""
		return a.name != b.name or a.sound != b.sound
