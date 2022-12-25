from collections import defaultdict, Counter
def groupAnagrams(words):
	hashmap = defaultdict(list)
	for word in words:
		key = checkAnagram(word) 
		hashmap[key].append(word)
	i = 0 
	for key in hashmap: 
		for word in hashmap[key]:
			words[i] = word
			i += 1

	return words


def checkAnagram(word):
	hashmap = Counter(word)
	key = ''
	for c in sorted(hashmap.keys()): 
		key += c + str(hashmap[c])
	return key 

words = ['hello', 'baaa', 'lloeh', 'abaa']
print(groupAnagrams(words))