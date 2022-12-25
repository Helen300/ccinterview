def sortedMerge(a, b):
	indexMerged = len(a) - 1
	indexB = len(b) - 1 
	# end of merged array 
	indexA = indexMerged - indexB - 1
	wr = indexMerged
	while indexB >= 0: 
		if indexA >= 0 and a[indexA] > b[indexB]:
			a[wr] = a[indexA]
			indexA -= 1
		else: 
			# print(indexB, wr)
			a[wr] = b[indexB]
			indexB -= 1
		wr -= 1
	return a

A_o = [1, 2, 3, 4]
B = [2, 4, 5, 6]
A = [0] * (len(A_o) + len(B))
A[:len(A_o)] = A_o

print(sortedMerge(A, B))
