from Base import Base

class Right(Base):
	def __init__(self):
		print "From Right class init"
		super(Right, self).__init__()
	def access_Right(self):
		print "From Right class"
	def common(self):
		print "From Right common method"
	def override(self):
		print "From Right override"
	
