## binary search algorithm takes a sorted
## array and a value and returns the value
## or null if value not present

def binary_search(sorted_arr, target):
    low = 0
    high = len(sorted_arr) - 1

    while low  <= high:
        # check middle element
        mid = (low + high) // 2 # int division
        search_val = sorted_arr[mid]
        if search_val == target:
            return mid
        ## check search_val
        elif search_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


a1 = [ 1, 5, 9, 12, 75, 8000, 100000001] # 12
a2 = [ 7373, 8484849, 438932945290, 23408320948239939393] # 8484849
a3 = [6, 12, 37, 92, 93, 104, 160, 176, 198, 202, 305, 380, 900] # 160
a4 = [1, 3, 5, 7 ,9]

print(binary_search(a2, 8484849))


