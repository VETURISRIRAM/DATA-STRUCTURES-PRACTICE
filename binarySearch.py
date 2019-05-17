inputList = [1,2,3,4,5,6,7,8,10]

target = 8
low = 0
high = len(inputList)

def binarySearch(inputList, target, high, low):
	
	if high <= low:
		return -1

	mid = int((high + low)/2)
	print(inputList[mid])

	if target == inputList[mid]:
		return mid

	if target < inputList[mid]:
		high = mid - 1
		return binarySearch(inputList, target, high, low)

	if target > inputList[mid]:
		low = mid + 1
		return binarySearch(inputList, target, high, low)


print("Target found at {}th index!".format(binarySearch(inputList, target, high, low)))