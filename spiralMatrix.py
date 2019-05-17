def spiral(matrix):
	m = len(matrix)
	n = len(matrix[0])
	
	direction = 0

	top, left = 0, 0
	bottom, right = m, n

	while top < bottom and left < right:

		if direction == 0:
			for i in range(left, right):
				print(matrix[top][i], end=' ')
			direction = 1
			top += 1

		if direction == 1:
			for i in range(top, bottom):
				print(matrix[i][right-1], end=' ')
			direction = 2
			right -= 1

		if direction == 2:
			for i in range(right - 1, left - 1, -1):
				print(matrix[bottom-1][i], end=' ')
			bottom -= 1
			direction = 3

		if direction == 3:
			for i in range(bottom - 1, top -1 , -1):
				print(matrix[i][left], end=' ')
			left += 1
			direction = 0






if __name__=="__main__":

	spiral([
 [ 1, 2, 3, 1 ],
 [ 4, 5, 6, 1 ],
 [ 7, 8, 9, 1 ]
])




	