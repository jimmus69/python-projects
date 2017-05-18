#! /usr/bin/env python
# class04.py 

class House:
	def __init__(self, number = "not defined", rooms = "not defined", garden = "not defined"):
		self.number = number
		self.rooms = rooms
		self.garden = garden

my_house = House(20, 1, 0)

print "My house is number", my_house.number
print "It has", my_house.rooms, "rooms"
hasString = "has" if my_house.garden else "does not have"
#print "It", "has" if my_house.garden else "does not have", "a garden"

print "It", hasString, "a garden"

your_house = House()
print "\nYour house is number", your_house.number
print "It has", your_house.rooms, "rooms"
