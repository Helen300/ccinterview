import collections

def permutations(s):
	results = []
	curr = ''
	recurse(s)
	return results

# EXAMPLE 
""" 
xy
recurse(xy)
first = x
remainder = y
words = ['y']
xy, yx


words = recurse(y) 
first = y 
remainder = ''
returning with words = ['']
for w in words: 
	for j in '':
		y
return [y]

words = recurse('')
return ['']
"""

def recurse(string):
	if string == None:
		return None
	perms = [] 
	if len(string) == 0: # base case
		perms.append("")
		# print("returning with remainder string ", string, " is ", perms)
		return perms
	first = string[0]
	remainder = string[1:]
	words = recurse(remainder)
	for w in words:
		for j in range(len(w) + 1):
			s = insertCharAt(w, first, j)
			perms.append(s)
	# print("returning with remainder string ", string, " is ", perms)
	return perms


def insertCharAt(word, c, i):
	start = word[0:i]
	end = word[i:]
	return start + c + end

def permutationsWithDups(s):
	all_perms = [] 
	mapping = collections.defaultdict(int)
	for c in s: 
		mapping[c] += 1
	findAllPerms(all_perms, '', len(s), mapping)
	return all_perms

def findAllPerms(all_perms, prefix, remainingChars, mapping):
	# Used up all chars, base case
	if remainingChars == 0: 
		all_perms.append(prefix[:])
		return 
	for char in mapping.keys():
		if mapping[char] != 0: 
			mapping[char] -= 1
			findAllPerms(all_perms, prefix + char, remainingChars-1, mapping)
			mapping[char] += 1

print("Normal Perm ", permutations('abc'))
print(permutationsWithDups('aab'))




