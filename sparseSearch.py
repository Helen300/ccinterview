def sparseSearch(arr, target):
	lo = 0 
	hi = len(arr) - 1
	empty_string = '' 

	while lo <= hi: 
		mid = (lo + hi) // 2
		# if mid is empty, find closest non-empty string 
		mid = helperForEmptyString(arr, mid, lo, hi)
		if arr[mid] == target: 
			return mid
		elif arr[mid] > target:
			hi = mid - 1
		elif arr[mid] < target:
			lo = mid + 1
	return -1 

def helperForEmptyString(arr, mid, lo, hi):
	if len(arr[mid]) == 0:
		left = mid - 1
		right = mid + 1
		while True:
			if left < lo and right > hi: 
				return -1 
			elif right <= hi and len(arr[right]) != 0:
				mid = right
				break
			elif left >= lo and len(arr[left]) != 0: 
				mid = left
				break 
			right += 1
			left -= 1
	return mid

arr = ['at', '', '', '', 'ball', '', '', '', 'car', '', '', 'dad', '', '']
target = 'ball'
print(sparseSearch(arr, target))