#! /usr/bin/python

class Bird(object):
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print 'Aaaaah...'
			self.hungry = False
		else:
			print 'No, thanks!'

class SongBird(Bird):
	def __init__(self):
		super(SongBird,self).__init__()
		self.sound = 'Squaak!'
	def sing(self):
		print self.sound

# main program

bird = SongBird()
bird.eat()
bird.eat()
bird.sing()

