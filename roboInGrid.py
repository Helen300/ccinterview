


def roboInGrid(maze):
	if not maze or len(maze) == 0:  
		return None
	rows = len(maze) - 1
	cols = len(maze[0]) - 1
	path = [] 
	visited = set()
	if getPath(maze, rows, cols, path, visited):
		return path
	return None

def getPath(maze, r, c, path, visited):
	if r < 0 or c < 0 or not maze[r][c]: 
		return False
	p = (r * len(maze)) + (c * len(maze[0]))
	# already previously visited
	if p in visited: 
		return False
	isAtOriginCheck = r == 0 and c == 0

	if (isAtOriginCheck or getPath(maze, r, c - 1, path, visited) 
		or getPath(maze, r - 1, c, path, visited)):
		visited.add(p)
		path.append((r,c))
		return True

	return False


maze = [[True, True, True, False], 
		[True, False, False, False], 
		[False, True, False, False], 
		[False, True, True, True]]

print(roboInGrid(maze))