
## recursive sum
def recursive_sum(list):
	if list == []:
		return 0
	return list[0] + recursive_sum(list[1:])

## recursive count
def recursive_count(arr):
	if arr == []:
		return 0
	return 1 + recursive_count(list[1:])


# def print_items(list):
#     for item in list:
#         print(item)

## quicksort
## pick a pivot
## partition array into two subarrays:
## elements less the pivot and
## elements greater than the pivot
## call quicksort recursively on the two subarrays

def quicksort(arr):
    ## drive towards base case
    if len(arr) < 2:
        return arr # array is tautologically sorted
    
    else: # recursive case
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(more)


a1 = [1, 7, 6, 12, 9]
a2 = [27, 5, 84, 148, 23]
a3 = [100, 4, 99, 17, 62]

t1 = quicksort(a1)
t2 = quicksort(a2)
t3 = quicksort(a3)

print(t1)
print("\n")
print(t2)
print("\n")
print(t3)