def genParens(n): 
	openp = 0
	closedp = 0
	curr = ''
	results = [] 
	recurse(openp, closedp, curr, results, n)
	return results


def recurse(openp, closedp, curr, results, n): 
	if len(curr) == (2 * n): 
		results.append(curr[:])
	# can always insert an open parentheses if less than total # of parentheses set
	if openp < n: 
		recurse(openp + 1, closedp, curr + '(', results, n)
	# can add closed parentheses if it its less than number of open parentheses 
	if closedp < openp: 
		recurse(openp, closedp + 1, curr + ')', results, n)


print(genParens(3))
