from array import *

# Declare an array
arrayName = array('i', [1,2,3,4,5])

for x in arrayName:
	print(x)

# Print elements by index
print(arrayName[1])

# Insert elements
arrayName.insert(1, 50)
print(arrayName)

# Remove elements
arrayName.remove(50)
print(arrayName)

# Search through the array
print(arrayName.index(4))

# Update elements
arrayName[4] = 60
print(arrayName)

# Two Dimensional array
t = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

for r in t:
	for x in r:
		print(x, end=" ")
	print()