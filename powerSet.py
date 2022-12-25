# computing P(N-1) and adding a_n to each of them 
# Space O(n ^ 2^n) in time and space for recursive approach
def powerSetIterative(arr):
	# if we have an empty set starting
	# then take each number and add it to each set
	# that we create in our all_subsets
	# then we get all power sets!
	subsets = [[]]
	for n in arr: 
		subsets += [s + [n] for s in subsets]
	return subsets

def powerSetBinary(arr):
	# 2^n possible subsets because each set has
	# the option of either existing ('yes')
	# or not existing ('no')
	# in the subset
	all_subsets = [] 
	# everytime we shift 1 to the right
	# we multiple by 2! 
	count_subsets = 1 << len(arr)
	for k in range(count_subsets):
		subset = convertIntToSet(k, arr)
		all_subsets.append(subset)
	return all_subsets

def convertIntToSet(num, arr):
	subset = [] 
	index = 0 
	k = num
	while k > 0: 
		if (k & 1) == 1: 
			subset.append(arr[index])
		index += 1
		k >>= 1
	return subset


print(powerSetIterative([1,2]))
print(powerSetBinary([1,2]))



