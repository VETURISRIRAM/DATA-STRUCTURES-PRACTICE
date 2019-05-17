nums = [-1, 0, 1, 2, -1, -4]
nums = [-4, -1, -1, 0, 1, 2]
output = []
nums = sorted(nums)

for x in range(0, len(nums)-1):
	i = x + 1
	j = len(nums)-1
	print(x)
	while i < j:
		sums = nums[i] + nums[j]
		
		if (nums[x] + sums) == 0:
			output.append([nums[x], nums[i], nums[j]])
			i += 1
			j -= 1

		elif sums > nums[x]:
			i += 1
		elif sums < nums[x]:
			j -= 1

print(output)

