# Coin Change problem from leetcode
# Time Complexity = O(A * C) where C = # of coins, A = Amount 
# Space = O(A) => just storing an array of length amount
def countCoins(coins, amount):
	countWays = [0] * (amount + 1)
	countWays[0] = 1
	for c in coins: 
		for i in range(amount+1):
			print("i", i, "c", c)
			if c <= i:
				countWays[i] += countWays[i - c]
	return countWays[amount]



coins = [1, 2]
amount = 5
print("amount of ways to make ", amount, " is ", countCoins(coins, amount))

""" 
Subproblems

========== Amount = 0 =========
1) Base Case, First Subproblem 
==> with coins = [] => amount = 0
==> there is exactly 1 way = do nothing!
==> doesn't matter what coins you give me
==> there is only one way! 
==> therefore for 
2) Case coins = [1], amount = 0 
==> still just one way!
3) Case coins = [1, 2], amount = 0 ways = 1
4) Case coins = [1, 2, 5], amount = 0 ways = 1 

========== Coins = [] =========
1) coins = [] amount = 1
==> there is NO way to make amount of 1 with no coins
==> ways = 0 

2) coins = [] amount = 2 ways = 0
3) coins = [] amount = 3 ways = 0
4) coins = [] amount = 4 ways = 0
5) coins = [] amount = 5 ways = 0

========== Amount = 1 =========
1) coins = [1] amount = 1
===> If I chose to use the coin [1]
===> I would need to find all ways of
===> not using coin + all ways of using that coin to make amount - coin 
===> not using coin (going back up a row) [] amount = 1 => ways = 0 
===> all ways of using that coin to make amount - coin = 1 - 1 = 0 ways = 1
===> now we have 0 + 1 = 1 way to make amount = 1 with coin = [1]

2) coins = [1] amount = 2
===> If i choose to use coin [1] 
===> then sum of all ways of using [1] to make amount = 2 is
===> ways to make [amount - coin] + not using coin to make amount
===> ways[1] = 1 + ways[2] via [] = 0 = 1 

3) coins = [1] amount = 3
===> If i choose to use coin [1] 
===> then sum of all ways of using [1] to make amount = 2 is
===> ways to make [amount - coin] + not using coin to make amount
===> ways[2] = 1 + ways[3] via [] = 0 = 1 

========== Coins = [1,2] =========
1) coins = [1, 2] amount = 1
===> cannot even use the 2 coin to make amount 1, because amount - coin < 0
===> therefore ways of using [1,2] to make amount = 1 ====
===> same as not using [2] and just using [1] to make amount = 1 

1) coins = [1, 2] amount = 2
===> can use the [2] to make amount = 2
===> we do amount - coin = 0 ways[0] with [2] + ways[2] without [2] or just [1] 
===> 1 + 1 = 2  


"""





