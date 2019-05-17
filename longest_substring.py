s = 'dvdf'

temp = ''
l = []
		
for char in s:
	if char not in temp:
		temp = temp + char
	else:
		index = temp.index(char)
		l.append(len(temp))
		temp = char
	print(temp)

l.append(len(temp))
# if l == []:
# 	print(len(temp))
# else:
# 	return max(l)
print(temp)
print(l)