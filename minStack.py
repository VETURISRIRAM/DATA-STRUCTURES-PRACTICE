class Stack:
	def __init__(self):
		self.stack = []
		self.minList = []
		self.minList.append(1000000)

	def push(self, val):
		if val < self.minList[-1]:
			self.minList.append(val)
		self.stack.append(val)

	def pop(self):
		if self.stack != []:
			if self.minList[-1] == self.stack[-1]:
				del(self.minList[-1])
			temp = self.stack[-1]
			del(self.stack[-1])
			return temp
		else:
			return None

	def printStack(self):
		for x in self.stack:
			print(x)

	def returnMin(self):
		print(self.minList[-1])

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.printStack()
s.returnMin()
s.pop()
s.returnMin()
s.pop()
s.returnMin()
s.pop()
s.returnMin()