class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def maxDepth(root):

	if root:
		left = maxDepth(root.left)
		right = maxDepth(root.right)

		if abs(left - right) > 1:
			flag = False

		return max(left, right) + 1
	else:
		return 0


root = Node(10)
root.left = Node(12)
root.right = Node(15)
# root.left.left = Node(25)
# root.left.left.left = Node(100)
# root.left.left.left.left = Node(125)
flag = True
print("Max Depth of the tree is ", maxDepth(root))

print(flag)