from Left import Left
from Right import Right

class Bottom(Left, Right):
	def __init__(self):
		print "From Bottom class init"
		super(Bottom, self).__init__()
	def access_Bottom(self):
		print "From Bottom class"
	
