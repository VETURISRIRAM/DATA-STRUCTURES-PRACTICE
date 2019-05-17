class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def identicalCheck(treeA, treeB):

	if treeA is None and treeB is None:
		return None

	if treeA is not None and treeB is not None:
		return ((treeA.data==treeB.data) and (identicalCheck(treeA.left, treeB.left)) and (identicalCheck(treeA.right, treeB.right)))

	return True	



treeA = Node(10)
treeA.left = Node(12)
treeA.right = Node(15)
treeA.left.left = Node(25)
treeA.left.right = Node(30)
treeA.right.left = Node(36)
treeA.right.left.left = Node(100)

treeB = Node(10)
treeB.left = Node(12)
treeB.right = Node(15)
treeB.left.left = Node(25)
treeB.left.right = Node(30)
treeB.right.left = Node(36)

print(identicalCheck(treeA, treeB))

