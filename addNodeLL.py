class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linkedList:
	def __init__(self, head):
		self.head = head

	def traversal(self):
		if self.head:
			element = self.head
			while element:
				print(element.data)
				element = element.next

	def addNodeStart(self, val):
		val.next = self.head
		self.head = val
		while val:
			print(val.data)
			val = val.next

	def addEndNode(self, val):
		element = self.head
		while element:
			print(element.data)
			element = element.next
		element = val
		print(element.data)


	def addNodeMiddle(self, val, ind):
		element = self.head
		counter = 0
		while element:
			if counter == ind-1:
				val.next = element.next
				element.next = val

			counter += 1




zeroth = Node(0)
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
middle = Node("Middle")
a.next = b
b.next = c
c.next = d

l = linkedList(a)

l.addNodeStart(Node(0))


# l.addEndNode(e)

# l.addNodeMiddle(middle, 2)

# l.traversal()

