def get_common_elements_first(a, b):

	m = len(a)
	n = len(b)

	common = []

	for i in range(0, m):
		for j in range(0, n):
			if a[i] == b[j]:
				if a[i] not in common:
					common.append(a[i])

	return common

def get_common_elements_second(a, b):

	common = []

	m = len(a)
	n = len(b)

	a = sorted(a)
	b = sorted(b)

	i = 0
	j = 0

	while i < m and j < n:

		if a[i] > b[j]:
			j += 1
		elif a[i] < b[j]:
			i += 1
		else:
			if a[i] not in common:
				common.append(a[i])
			i += 1
			j += 1

	return common


def get_common_elements_hash(a, b):

	common = []

	a_hash_map = {}
	b_hash_map = {}
	both_hash_map = {}

	for i in range(0, len(a)):
		if a[i] not in a_hash_map:
			a_hash_map[a[i]] = 1
		else:
			a_hash_map[a[i]] += 1

		if a[i] not in both_hash_map:
			both_hash_map[a[i]] = 1
		else:
			both_hash_map[a[i]] += 1



	for j in range(0, len(b)):
		if b[j] not in b_hash_map:
			b_hash_map[b[j]] = 1
		else:
			b_hash_map[b[j]] += 1

		if b[j] not in both_hash_map:
			both_hash_map[b[j]] = 1
		else:
			both_hash_map[b[j]] += 1

	for element, count in both_hash_map.items():

		if element in a_hash_map:
			if both_hash_map[element] != a_hash_map[element]:
				if element not in common:
					common.append(element)
		if element in b_hash_map:
			if both_hash_map[element] != b_hash_map[element]:
				if element not in common:
					common.append(element)

	return common

if __name__ == "__main__":

	array1 = [1,2,3,4,5,6,7,9]
	array2 = [3,4,8,3,9,0,13]

	print("First Method:")
	print(get_common_elements_first(array1, array2))

	print("\nSecond Method:")
	print(get_common_elements_second(array1, array2))

	print("\nThird Method:")
	print(get_common_elements_hash(array1, array2))