def paintFill(screen, r, c, color):
	recurse(screen, r, c, color)
	return screen

def paintFillA(screen, r, c, color):
	rows = len(screen)
	cols = len(screen[0])
	if r < 0 or r >= rows or c < 0 or c >= cols: 
		return 

	if screen[r][c] != color:
		screen[r][c] = color
		next_pos = [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]
		for nr, nc in next_pos: 
			paintFillA(screen, nr, nc, color)


screen = [[1, 2, 9], [3, 4, 8], [5, 6, 7]]
color = -1
r = 2
c = 2
print("before: ", screen)
paintFillA(screen, r, c, color)
print("after: ", screen)