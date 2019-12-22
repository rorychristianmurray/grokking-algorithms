## selection sort moves through a list and selects the largest item
## and places it into a new list. It then repeats this process
## until the list is sorted

## selection sort runs in O(n^2) time

def find_smallest(arr):
	smallest = arr[0] # get first element from array
	smallest_index = 0 # track index of smallest element

	for i in range (1, len(arr)): # run from next element to end of list
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i

	return smallest_index



def selection_sort(arr):
	new_arr = []
	for i in range(len(arr)):
		smallest = find_smallest(arr)
		new_arr.append(arr.pop(smallest))
	return new_arr

l1 = [32, 7, 19, 4, 16, 102]

t1 = selection_sort(l1)

print(t1)
