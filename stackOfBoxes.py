def stackOfBoxes(boxes):
	# sort by height? 
	def byHeight(x):
		return x.height
	boxes = sorted(boxes, key=byHeight, reverse=True)
	maxheight = 0 
	for i in range(len(boxes)): 
		height = createStack(boxes, i)
		maxheight = max(maxheight, height)
	return maxheight

def createStack(boxes, bottomBox):
	bottom = boxes[botttomBox]
	maxheight = 0 
	# start the next box as bottom and see what can be built above it
	for i in range(bottomBox+1, len(boxes)):
		if canBeStacked(boxes[i], bottom):
			height = createStack(boxes, i)
			maxheight = max(maxheight, height)
	maxheight += bottom.height
	return maxheight

def canBeStacked(boxTop, boxBottom):
	if boxTop.height > boxBottom.height or boxTop.width > boxBottom.width /
	or boxTop.depth > boxBottom.depth:
		return False
	return True

