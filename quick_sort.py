def get_pivot(array, low, high):

	mid = (low + high) // 2
	median_pivot = sorted([array[low], array[high], array[mid]])[1]

	return median_pivot, array.index(median_pivot)


def get_partition(array, pivot_index, low, high):

	if low < high:

		start = low
		if array[pivot_index] != array[start]:

			array[start], array[pivot_index] = array[pivot_index], array[start]

		border = array[start + 1]
		border_index = start + 1

		for element_index in range(2, len(array)):

			if array[element_index] > array[pivot_index]:

				array[border_index], array[element_index] = array[element_index], array[border]
				border_index += 1

		array[pivot_index], array[border_index] = array[border_index], array[pivot_index]

		return border_index

	else:

		return -1



def quick_sort_helper(low, high, array):

	pivot, pivot_index = get_pivot(array, low, high)
	border_index = get_partition(array, pivot_index, low, high)

	if border_index == -1:
		return array

	left = array[:border_index]
	quick_sort_helper(low, border_index, array)
	right = array[border_index:]
	quick_sort_helper(border_index, high, array)





def quick_sort(array):

	low = 0
	high = len(array) - 1
	
	quick_sort_helper(low, high, array)

	return array





if __name__ == "__main__":

	a = [17, 41, 5, 22, 54, 6, 29, 3, 13]

	print("Unsorted array : ", a)
	print()
	print("Sorted array : ", quick_sort(a))