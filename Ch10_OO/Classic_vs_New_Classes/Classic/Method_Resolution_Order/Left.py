from Base import Base

class Left(Base):
	def __init__(self):
		print "From Left class init"
		Base.__init__(self)
	def access_Left(self):
		print "From Left class"
	def common(self):
		print "From Left common method"
	def override(self):
		print "From Left class"
