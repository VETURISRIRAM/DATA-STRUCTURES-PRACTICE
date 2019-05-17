# Pointers in Python
class Nodes:
	def __init__(self, dataval=None):
		self.dataval = dataval
		self.nextval = None

e1 = Nodes('Monday')
e2 = Nodes('Tuesday')
e3 = Nodes('Wednesday')

e1.nextval = e2
e2.nextval = e3

thisvalue = e1

while thisvalue:
	print(thisvalue.dataval)
	thisvalue = thisvalue.nextval