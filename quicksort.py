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