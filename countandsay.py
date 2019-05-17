def count_and_say(n):

	if n == 1:
		return '1'
	elif n == 2:
		return '11'
	elif n == 3:
		return '21'

	s = '21'

	for number in range(3, n):

		new = ""
		count = 1
		i = 1

		while i < len(s):
			if s[i-1] == s[i]:
				count += 1
				i += 1
				continue
			else:
				new += str(count) + s[i-1]
				i += 1
				count = 1

		new += str(count) + s[-1]
		s = new
		print(s)
	return s

print("\nAnswer is: ", count_and_say(6))
