class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

head = ListNode(10)
temp = head
head.next = ListNode(12)
head = head.next
head.next = ListNode(11)
head = head.next
head.next = ListNode(11)
head = head.next
head.next = ListNode(12)
head = head.next
head.next = ListNode(11)
head = head.next
head.next = ListNode(10)
head = head.next


head = temp

def remove_duplicates(head):

	final = head
	helper = []
	

	while head:

		if head.next.val in helper:
			head.next = head.next.next
			
		else:
			helper.append(head.val)

		head = head.next

	return final

l = remove_duplicates(head)
while l:
	print(l.val)
	l = l.next





# final = head
# hash_map = []
# hash_map.append(head.val)
# while head:
# 	if head.next.val not in hash_map:
# 		hash_map.append(head.next.val)
		

# 	else:

# 		if head.next:

# 			head.next = head.next.next

# 		else:
# 			head.next = None

# 	head = head.next
# while final:
# 	print(final.val)
# 	final = final.next


def shopppers(inputList):
	
	i = 0
	d = {}

	while i < len(inputList):
		if inputList[i] not in d:
			lengths = []
			targetChar = inputList[i]

			j = len(inputList) - 1

			found_at = -99999
			while j >= 0:
				if inputList[j] == targetChar:
					if j > found_at:
						found_at = j
						break
				j -= 1
			d[inputList[i]] = {'first': i, 'last': found_at}
		i += 1

	for shoppers, indices in d.items():
		last_position = indices['last']
		

	print(d)



print(shopppers(['a','b', 'a', 'c','d']))