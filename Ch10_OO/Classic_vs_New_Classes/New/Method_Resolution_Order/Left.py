from Base import Base

class Left(Base):
	def __init__(self):
		print "From Left class init"
		super(Left, self).__init__()
	def access_Left(self):
		print "From Left class"
	def common(self):
		print "From Left common method"
	
