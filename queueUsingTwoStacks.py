class TwoStacks:
	def __init__(self):
		self.stackA = []
		self.stackB = []

	def push(self, val):
		self.stackA.append(val)

	def pop(self):
		self.stackB = []
		if self.stackA != []:
			
			self.stackB = self.stackA[::-1]

			temp = self.stackB[-1]
			del(self.stackB[-1])
			del(self.stackA[0])
			return temp
		else:
			return None

	def printQueue(self):
		for x in self.stackB:
			print(x)

S = TwoStacks()
S.push(1)
S.push(2)
S.push(3)

print("Popped item is {}".format(S.pop()))
print("Popped item is {}".format(S.pop()))
# print("Popped item is {}".format(S.pop()))
# print("Popped item is {}".format(S.pop()))
#print("The Queue is {}".format(S.printQueue()))