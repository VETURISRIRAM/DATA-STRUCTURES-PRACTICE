class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def inOrderTraversal(root):
	if root.left:
		inOrderTraversal(root.left)

	if root:
		print(root.data)
		l.append(root.data)

	if root.right:
		inOrderTraversal(root.right)

def greaterTree(root):
	
	if root:

		s = 0
		inOrderTraversal(root)
		

root = Node(10)
root.left = Node(8)
root.right = Node(15)
# root.left.left = Node(25)
# root.left.right = Node(30)
# root.right.left = Node(36)

# print("Inorder Traversal -->")
# inOrderTraversal(root)

print('Greater Tree -->')
l = []
if root:

	if root.right:
		greaterTree(root.right)
		root.right.data = sum(l)

