def towersOfHanoi(n, origin, dest, aux):
	"""
	The idea is to use the helper node to reach the destination using recursion. Below is the pattern for this problem:

	Shift ‘N-1’ disks from ‘A’ to ‘B’, using C.
	Shift last disk from ‘A’ to ‘C’.
	Shift ‘N-1’ disks from ‘B’ to ‘C’, using A.
	"""
	if n <= 0:
		return
	towersOfHanoi(n-1, origin, aux, dest)
	moveLast(origin, dest)
	towersOfHanoi(n-1, aux, dest, origin)

def moveLast(fro, to):
	last = fro.pop()
	to.append(last)

n = 6
A = [1,2,3,4,5,6]
C = []
B = []
print("Before: ", A, B, C)
towersOfHanoi(n, A, C, B)
print("After: ", A, B, C)