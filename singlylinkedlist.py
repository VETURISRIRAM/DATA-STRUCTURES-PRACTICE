class Node:
	def __init__(self, dataval=None):
		self.dataval = dataval
		self.nextval = None

class SinglyLinkedList:
	def __init__(self, headval=None):
		self.headval = headval

	def printList(self):
		element = self.headval
		while element != None:
			value = element.dataval
			print(value)
			element = element.nextval

	def insertStart(self, newElement):
		initialValue = self.headval
		self.headval = newElement
		self.headval.nextval = initialValue

	def insertEnd(self, newElement):
		element = self.headval
		while element != None:
			value = element.dataval
			element = element.nextval
			if element.nextval == None:
				element.nextval = newElement
				break

	def delMiddle(self, delNode):
		element = self.headval

		while element:
			if element.dataval == delNode:
				element.nextval = element.nextval.nextval
			else:
				element = element.nextval
		
e0 = Node("Sunday")
e1 = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")
e5 = Node("Friday")


e1.nextval = e2
e2.nextval = e3

l1 = SinglyLinkedList(e1)

#SinglyLinkedList.printList(l1)

SinglyLinkedList.insertStart(l1, e0)
SinglyLinkedList.insertEnd(l1, e5)
SinglyLinkedList.printList(l1)

SinglyLinkedList.delMiddle(l1, "Tuesday")