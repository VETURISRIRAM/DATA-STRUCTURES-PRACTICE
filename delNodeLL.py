class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linkedList:
	def __init__(self, head):
		self.head = head

	def traversal(self):
		element = self.head
		while element:
			print(element.data)
			element = element.next

	def delNode(self, ind):
		
		element = self.head
		while element:
			if element.next.data == ind:
				element.next = element.next.next

			
			break
			

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

l = linkedList(a)
l.delNode(5)
l.traversal()
