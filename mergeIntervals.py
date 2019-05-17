def mergeIntervals(intervals):

	
	# Sort based on start of interval
	d = {}
	for i in intervals:
		d[i[0]] = i[1]
	print(d)
	sortedIntervals = sorted(d)
	print(sortedIntervals)
	hashMap = {}
	for i in sortedIntervals:
		hashMap[i] = d[i]
	print(hashMap)
	l = []
	for key, value in hashMap.items():
		l.append(key)
		l.append(value)

	# Insert first interval
	stack = []
	# stack.append(l[0])
	# stack.append(l[1])
	c = 0

	for start in hashMap:
		if c < 1:
			stack.append(start)
			stack.append(hashMap[start])
			c += 1
		
		# Pop the last of previous interval
		last = stack.pop()

		# Check if start of next is greater than last of previous
		if start > last:
			stack.append(last)
			stack.append(start)
			stack.append(hashMap[start])

		else:
			if last >= hashMap[start]:
				stack.append(last)
			else:
				stack.append(hashMap[start])

	print(stack) 
	final = []
	for x in range(0, len(stack), 2):
		final.append([stack[x], stack[x+1]])

	print(final)

	














	


if __name__=="__main__":

	intervals = [[1,3],[0,6],[8,10],[15,18]]

	merged = mergeIntervals(intervals)

	print("Merged Intervals are : {}".format(merged))



