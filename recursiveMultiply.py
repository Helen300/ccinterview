# Runs in O(log s) where s == smaller of the two nums

def recursiveMultiply(a, b):
	bigNum = b if a < b else a 
	smallNum = a if a < b else b
	return helper(smallNum, bigNum)

def helper(small, big): 
	if small == 0:
		return 0
	# working from small problems to big 
	if small == 1: 
		return big 
	
	half = small >> 1
	halfProd = helper(half, big)

	if small % 2 == 0:
		return halfProd + halfProd
	else:
		# if not even ex. 31 = 2 * 15 + 1
		return halfProd + halfProd + bigger 

# Example (3 x 4)
"""

bigNum = 4
smallNum = 3

helper(small, big) = helper(3, 4)
half = small >> 1 = 1
halfProd = helper(1, 4) = 4

if small % 2 == 0: return halfProd + halfProd
else: return halfProd + halfProd + bigger = 4 + 4 + 4 = 12

# Imagine this multiplication as counting the 1x1 squares
# in an a x b shape
# we can count half the squares and then double it... 


# Example (31, 35)
bigNum = 35
smallNum = 31

helper(31, 35)
half = 31 >> 1 = 31 // 2 = 15 
=> 525 + 525 + 35 = (1085)

helper(15, 35)
half = 15 >> 1 = 7
=> 245 + 245 + 35 = (35 x 15)

helper(7, 35)
half = 7 >> 1 = 3
=> 105 + 105 + 35 = (35 x 7) 

helper(3, 35)
half = 3 >> 1 = 1
=> after returning 35 from next call
=> 35 + 35 + 35 (this is the same as 3 x 35) 

helper (1, 35)
returns big = 35 (a x 1)


"""