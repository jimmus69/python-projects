from Left import Left
from Right import Right

class Bottom(Left, Right):
	def __init__(self):
		print "From Bottom class init"
		Left.__init__(self)
		Right.__init__(self)
	def access_Bottom(self):
		print "From Bottom class"
	
