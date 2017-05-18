#! /usr/bin/python
"""
class07 definition
"""

class House:
	number_of_houses = 0
	def __init__(self, number = "not defined", rooms = "not defined", garden = "not defined"):
		self.number = number
		self.rooms = rooms
		self.garden = garden
		House._add_house()
	
	@classmethod
	def _add_house(cls):
		cls.number_of_houses +=1

	@staticmethod
	def convert( data_in):
		if data_in == "not defined":
			return "<not defined>"

		
	

my_house = House(20, 1, 0)

print "My house number is ", my_house.number
print "It has", my_house.rooms, "rooms"
if my_house.garden:
	garden_text = "has"
else:
	garden_text = "does not have"
print "It", garden_text, "a garden"
print "The number of houses:", my_house.number_of_houses

your_house = House()
print "\nYour house number is", your_house.number
print "It has", House.convert(your_house.rooms), "rooms"
print "The number of houses:", your_house.number_of_houses
