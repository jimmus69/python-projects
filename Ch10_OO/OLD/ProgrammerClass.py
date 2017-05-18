from PersonClass import *

class Programmer(PersonClass):
	"""
	  Programer class with know language
	"""

	def __init__(self, inName, inCountry, inLanguage):
		PersonClass.__init__(self, inName, inCountry)
		self.language = inLanguage

	def get_language(self):
		return self.language

	def set_language(self, inLanguage):
		self.language = inLanguage


