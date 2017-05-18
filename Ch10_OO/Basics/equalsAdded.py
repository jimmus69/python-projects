#! /usr/bin/env python
"""
File:  equalsAdded.py
Traditional class definition
"""

class House:
	def __init__(self, number, rooms, garden):
		self.number = number
		self.rooms = rooms
		self.garden = garden
	def __eq__(self, other):
		if self.rooms == other.rooms and self.garden == other.garden:
			return True
		else:
			return False

my_house = House(20, 1, 0)

print "My house is number", my_house.number
print "It has", my_house.rooms, "rooms"
if my_house.garden:
	garden_text = "has"
else:
	garden_text = "does not have"
print "It", garden_text, "a garden"

other_house = House(25,1,0)

if my_house == other_house:
	print "The houses are the same"
else:
	print "The houses are different"

