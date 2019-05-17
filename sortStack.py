class SortStack:
	def __init__(self):
		self.stack = []
		self.temp = []

	def push(self, val):

		def sort():
			print(self.stack)

		self.stack.append(val)

		sort(self.stack)

S = SortStack()
S.push(1)

