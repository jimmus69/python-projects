class Animal(object):
	"""
	An animal that has a name
	"""
	def __init__(self, name):
		self.__name = name
	def get_name(self):
		return self.__name
	def set_name(self, name):
		self.__name = name
	name = property(get_name, set_name)

	def __str__(self):
		return self.__name

	def talk(self):
		print "Generic Animal Sound"
