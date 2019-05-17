class Queue:
	def __init__(self):
		self.queue = []
	def push(self, dataval):
		if dataval not in self.queue:
			self.queue.append(dataval)
			return True
		else:
			return False
	def pop(self):
		if len(self.queue) == 0:
			return "Empty Queue"
		else:
			poppedElement = self.queue[-1]
			del self.queue[-1]
			return poppedElement
	def peak(self):
		return self.queue

firstQueue = Queue()
firstQueue.push("Monday")
firstQueue.push("Tuesday")
firstQueue.push("Wednesday")
print(firstQueue.peak())
print(firstQueue.pop())
print(firstQueue.peak())		
