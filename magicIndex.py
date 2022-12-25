def magicIndex(arr):
	# arr is a sorted array 
	lo = 0
	hi = len(arr) - 1
	while lo < hi: 
		mid = (lo + hi) // 2
		if arr[mid] == mid: 
			return mid
		# if the value is greater than index
		# this means that our target must be on the left side
		# there is no way that we will find our target if we keep
		# going to the right side because the value >>> index 
		if arr[mid] > mid: 
			hi = mid - 1
		# if value is less than index
		# our target must on the right side
		# we still haven't found the cross where value == index 
		elif arr[mid] < mid:
			lo = mid + 1
	return lo

def magicIndexRecurse(arr):
	return recurse(arr, 0, len(arr)-1)


def recurse(arr, start, end):
	if end < start:
		return -1 
	midIndex = (start + end) // 2
	midVal = arr[midIndex]
	if midIndex == midVal:
		return midIndex
	elif midVal > midIndex:
		return recurse(arr, start, midIndex - 1)
	elif midVal < midIndex:
		return recurse(arr, midIndex + 1, end)

def magicIndexDup(arr):
	# arr is a sorted array but with duplicates 
	return magicIndexSearch(arr, 0, len(arr)-1)

def magicIndexSearch(arr, start, end):
	if end < start:
		return -1 
	midIndex = (start + end) // 2
	midVal = arr[midIndex]
	if midIndex == midVal:
		return midIndex

	# recursively search left and right 
	# see if we find one on the left 
	leftIndex = min(midIndex - 1, midVal)
	left = magicIndexSearch(arr, start, leftIndex)
	if left >= 0: 
		return left


	# see if we find one on the right 
	rightIndex = max(midIndex + 1, midVal)
	right = magicIndexSearch(arr, rightIndex, end)
	return right
	

print(magicIndex([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]))
print(magicIndexRecurse([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]))
print(magicIndexDup([-10, -5, 2, 2, 2, 3, 4, 5, 9, 12, 13]))