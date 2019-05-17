def findPivot(array, low, high):

	if high == low:
		return low

	if high < low:
		return -1

	mid = (high + low)//2

	if array[mid + 1] < array[mid]:
		return mid

	if array[mid] < array[mid - 1]:
		return mid - 1

	if array[mid] > array[high]:
		low = mid + 1
		return findPivot(array, low, high)

	if array[mid] < array[high]:
		high = mid - 1
		return findPivot(array, low, high)

def binarySearch(array, low, high, target):

	if high < low:
		return -1

	mid = int((low + high) / 2)

	if array[mid] == target:
		return mid

	if array[mid] < target:
		high = mid - 1
		return binarySearch(array, low, high, target)

	if array[mid] > target:
		low = mid + 1
		return binarySearch(array, low, high, target)


def pivotedBinarySearch(array, n, target):

	pivot = findPivot(array, 0, n-1)

	if pivot == -1:
		return binarySearch(array, 0, n - 1, target)

	if target == array[pivot]:
		return pivot

	if target < array[pivot]:
		return binarySearch(array, 0, pivot - 1, target)

	if target > array[pivot]:
		return binarySearch(array, pivot + 1, n - 1, target)



array = [4,5,6,7,0,1,2, 3]
n = len(array)
target = 1

print("Target found at {}th position!".format(pivotedBinarySearch(array, n, target)))