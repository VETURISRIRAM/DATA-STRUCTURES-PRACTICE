class Stack:
	def __init__(self):
		self.stack = []
	def push(self, dataval):
		if dataval not in self.stack:
			self.stack.append(dataval)
			return True
		else:
			return False
	def peak(self):
		return self.stack
	def pop(self):
		if len(self.stack) == 0:
			return False
		else:
			poppedItem = self.stack[0]
			del self.stack[0]
			return poppedItem

firstStack = Stack()
firstStack.push("Monday")
firstStack.push("Tuesday")
print(firstStack.peak())
print(firstStack.pop())