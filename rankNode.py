class RankNode: 
	def __init__(self, data):
		self.leftSize = 0 
		self.leftNode = None
		self.rightNode = None
		self.data = data

	def insert(self, d):
		if d <= self.data:
			if (self.leftNode != None):
				self.leftNode.insert(d)
			else:
				self.leftNode = RankNode(d)
			self.leftSize += 1
		else:
			if (self.rightNode != None):
				self.rightNode.insert(d)
			else:
				self.rightNode = RankNode(d) 

	def getRank(self, d):
		if d == self.data:
			return self.leftSize
		if d < self.data: 
			if self.leftNode == None:
				return -1
			return self.leftNode.getRank(d)
		else: 
			if self.rightNode == None:
				return -1
			else: 
				# we move to the right and get rank from right node
				# add everything from left side + rank from right node + 1
				return self.leftSize + self.rightNode.getRank(d) + 1

class Solution():
	def __init__(self):
		self.root = None
		self.track(20)
		# Should be 0
		print("Rank of 20 is ", self.getRankOfNum(20))
		self.track(15)
		self.track(10)
		# Should be 2
		print("Rank of 20 is ", self.getRankOfNum(20))
		self.track(25)
		# Should be 2
		print("Rank of 20 is ", self.getRankOfNum(20))
		self.track(23)
		self.track(24)
		# Should be 2
		print("Rank of 20 is ", self.getRankOfNum(20))
		self.track(13)
		self.track(5)
		# Should be 4
		print("Rank of 20 is ", self.getRankOfNum(20))
		print("Rank of 25 is ", self.getRankOfNum(25))

	def track(self, d):
		if self.root == None:
			self.root = RankNode(d)
		else:
			self.root.insert(d)

	def getRankOfNum(self, d):
		return self.root.getRank(d)

Solution()



