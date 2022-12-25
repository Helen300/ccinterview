def nQueens(n):
	# n = the n x n grid with n queens
	# can just track via an array of columns where 
	# each column stores which row contains the queen
	result = [] 
	placement = []
	solveQueens(n, 0, placement, result)
	return result 

def solveQueens(n, r, colPlacements, result):
	# GOAL! Or our base case / end case
	# when we've placed all our queens on each row
	if r == n: 
		result.append(colPlacements[:])
	# otherwise, determine next valid placement for a queen
	# on this row = r 
	else: 
		for c in range(n):
			# our choice of where to place the queen for this current row
			# in which column shall we place it
			colPlacements.append(c)
			# our constraint => can only place if not in same diagonal, row, col
			# as any other previously placed queens 
			if isValid(colPlacements):
				solveQueens(n, r + 1, colPlacements, result)
			# undo our choice 
			colPlacements.pop()

def isValid(colPlacements):
	currRow = len(colPlacements) - 1
	currCol = colPlacements[currRow]
	for r in range(currRow):
		# checking for diagonal 
		col = colPlacements[r]
		# two rows cannot have a queen in the same column 
		if col == currCol:
			return False
		# check diagonals
		# if distance between columns == dist between rows
		# they are in the same diagonal 
		diffCol = abs(col - currCol)
		diffRow = currRow - r
		if diffCol == 0 || diffCol == diffRow:
			return False
	return True



