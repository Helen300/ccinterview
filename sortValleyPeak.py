def sortValleyPeak(arr):
	for i in range(1, len(arr)-2):
		if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
			bigger = max(arr[i-1], arr[i+1])
			smaller = min(arr[i-1], arr[i+1])
			arr[i], arr[i-1], arr[i+1] = bigger, arr[i], smaller
	return arr


arr = [5, 3, 1, 2, 3]
print(sortValleyPeak(arr))
