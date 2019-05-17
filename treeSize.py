class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def sizeOfTree(root):
	if root:
		return (sizeOfTree(root.left) + sizeOfTree(root.right) + 1)
	else:
		return 0

root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)

print("The size of the tree is {}".format(sizeOfTree(root)))

