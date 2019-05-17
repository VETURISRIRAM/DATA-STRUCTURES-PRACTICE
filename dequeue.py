class Dequeue:
	def __init__(self):
		self.dequeue = []
	def peak(self):
		return self.dequeue
	def pushRight(self, dataval):
		if dataval not in self.dequeue:
			self.dequeue.append(dataval)
			return True
		else:
			return False
	def popRight(self):
		if len(self.dequeue) == 0:
			return "Empty Dequeue"
		else:
			poppedElement = self.dequeue[-1]
			del self.dequeue[-1]
			return poppedElement
	def pushLeft(self, dataval):
		if dataval not in self.dequeue:
			self.dequeue = [dataval] + self.dequeue
			return True
		else:
			return False
	def popLeft(self):
		if len(self.dequeue) == 0:
			return "Empty Dequeue"
		else:
			poppedElement = self.dequeue[0]
			del self.dequeue[0]
			return poppedElement

firstDequeue = Dequeue()
firstDequeue.pushLeft("Tuesday")
firstDequeue.pushLeft("Monday")
firstDequeue.pushRight("Wednesday")
print(firstDequeue.peak())

firstDequeue.popLeft()
print(firstDequeue.peak())
firstDequeue.popRight()
print(firstDequeue.peak())