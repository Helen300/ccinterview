def sortedSearch(arr, x):
	lo = 0 
	hi = 100
	while lo <= hi:
		mid = (lo + hi) // 2
		if arr[mid] == x: 
			return mid 
		if arr[mid] == -1 or arr[mid] > x
			hi = mid - 1
		else: 
			lo = mid + 1 
	return -1 
