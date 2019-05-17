class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def inOrderTraversal(root):
	if root.left is None:
		pass
	else:
		inOrderTraversal(root.left)
	if root is None:
		pass
	else:
		print(root.data)

	if root.right is None:
		pass
	else:
		inOrderTraversal(root.right)

def preOrderTraversal(root):
	if root is None:
		pass
	else:
		print(root.data)

	if root.left is None:
		pass
	else:
		preOrderTraversal(root.left)

	if root.right is None:
		pass
	else:
		preOrderTraversal(root.right)

def postOrderTraversal(root):
	if root.left is None:
		pass
	else:
		postOrderTraversal(root.left)

	if root.right is None:
		pass
	else:
		postOrderTraversal(root.right)

	if root is None:
		pass
	else:
		print(root.data)

root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)

print("Inorder Traversal -->")
inOrderTraversal(root)

print("Preorder Traversal -->")
preOrderTraversal(root)

print("Postorder Traversal -->")
postOrderTraversal(root)


