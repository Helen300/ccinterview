def searchRotatedArray(arr, target):
	lo = 0 
	hi = len(arr) - 1
	while lo <= hi: 
		mid = (lo + hi) // 2
		if arr[mid] == target:
			return mid
		if arr[mid] > arr[lo]: # this is the sorted section
			# so we can just compare to midpoint
			if arr[mid] > target:
				hi = mid - 1
			else:
				lo = mid + 1
		else:
		# not sorted section so mid < lo and theres some rotation going on
		# but this means that the right half must be somewhat sorted
		# so we can just compare to value at hi 
			if arr[mid] < target and target <= arr[hi]:
				lo = mid + 1
			else:
				hi = mid - 1
	return -1

arr = [10, 14, 15, 16, 19, 20, 25, 1, 3, 4, 5, 7]
target = 16
print(searchRotatedArray(arr, target))

'''
EXAMPLE

arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
lo = 0 hi = 11
mid = 5
arr[5] = 1 != target = 5
arr[mid=5]=1 < arr[lo=0]=15 and target=5 < arr[lo=0]=15
we move lo = mid + 1 = 6

sub_arr = 15, 16, 19, 20, 25, 1, [3, 4, 5, 7, 10, 14]
lo = 6 hi = 11
mid = 8 





'''



