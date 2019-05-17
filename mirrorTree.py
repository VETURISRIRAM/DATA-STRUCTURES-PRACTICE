class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def mirrorTree(root):
	if root:
		mirrorTree(root.left)
		mirrorTree(root.right)

		temp = root.left
		root.left = root.right
		root.right = temp
		

def printTree(root):
	if root:
		printTree(root.left)
		print(root.data)
		printTree(root.right)


root = Node(10)
root.left = Node(12)
root.right = Node(15)

print("Initial Tree : ")
printTree(root)

mirrorTree(root)

print("Mirrored Tree : ")
printTree(root)