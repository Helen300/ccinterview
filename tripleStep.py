# coding=utf-8

"""Recursive & Dynamic Programming."""

n = input()


def tripleStep(n):
	# Q: For n = 0, would that be 0 steps?
	# Q: For n = 1, that would just be 1 step
	if n == 1:
		return 1
	if n == 0:
		return 1
	if n < 0: 
		return 0
	return tripleStep(n - 1) + tripleStep(n - 2) + tripleStep(n - 3)

def tripleStepMemo(n):
	memo = [-1] * (n + 1)
	return tripleStepMem(n, memo)

def tripleStepMem(i, memo):
	if i == 0:
		 return 1
	if i < 0: 
		return 0
	if (memo[i] == -1):
		memo[i] = tripleStepMem(i - 1, memo) + tripleStepMem(i - 2, memo) + tripleStepMem(i-3, memo) 
	return memo[i]

def tripleStepDP(n):
	if n == 0: 
		return 1
	memo = [0] * (n + 1)
	memo[0] = 1 
	memo[1] = 1
	memo[2] = 2

	for i in range(3, n + 1):
		memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
	return memo[n]



def countWays(n):
	memo = [-1] * (n + 1)
	return countWays2(n, memo)

def countWays2(n, memo):
	if (n < 0):
		return 0
	elif (n == 0):
		return 1
	elif (memo[n] > -1):
		return memo[n];
	else:
		memo[n] = countWays2(n - 1, memo) + countWays2(n - 2, memo) + countWays2(n - 3, memo)
	return memo[n]



print("tripleStep", tripleStep(int(n)))
print("tripleStepMemo", tripleStepMemo(int(n)))
print("tripleStepDP", tripleStepDP(int(n)))
print("solution Count Ways", countWays(int(n)))