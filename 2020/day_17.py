import numpy as np

def expandMatrix3(mtx, c):
	size = mtx.shape
	new_mtx = np.full((2*c+1, size[0]+2*c, size[1]+2*c), '.')
	new_mtx[c+1, c:c+size[0], c:c+size[1]] = mtx
	return new_mtx

def expandMatrix4(mtx, c):
	size = mtx.shape
	new_mtx = np.full((2*c+1, 2*c+1, size[0]+2*c, size[1]+2*c), '.')
	new_mtx[c+1, c+1, c:c+size[0], c:c+size[1]] = mtx
	return new_mtx

def checkNeighborhood3(z, y, x, space):
	n = 0
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			for k in [-1, 0, 1]:
				if i == 0 and j == 0 and k == 0:
					continue
				try:
					if space[z+i, y+j, x+k] == '#':
						n += 1
				except:
					pass
	return n

def checkNeighborhood4(w, z, y, x, space):
	n = 0
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			for k in [-1, 0, 1]:
				for l in [-1, 0, 1]:
					if i == 0 and j == 0 and k == 0 and l == 0:
						continue
					try:
						if space[w+i, z+j, y+k, x+l] == '#':
							n += 1
					except:
						pass
	return n


def task1(mtx):
	space = expandMatrix3(mtx, 6)
	for a in range(1, 7):
		next = np.full(space.shape, '.')
		for z in range(space.shape[0]):
			for y in range(space.shape[1]):
				for x in range(space.shape[2]):
					neighbors = checkNeighborhood3(z, y, x, space)
					if (space[z, y, x] == '.') and (neighbors == 3):
						next[z, y, x] = '#'
					elif (space[z, y, x] == '#') and (neighbors == 3 or neighbors == 2):
						next[z, y, x] = '#'
		space = next.copy()
	return np.count_nonzero(space == '#')

def task2(mtx):
	space = expandMatrix4(mtx, 6)
	for a in range(1, 7):
		next = np.full(space.shape, '.')
		for w in range(space.shape[0]):
			for z in range(space.shape[1]):
				for y in range(space.shape[2]):
					for x in range(space.shape[3]):
						neighbors = checkNeighborhood4(w, z, y, x, space)
						if (space[w, z, y, x] == '.') and (neighbors == 3):
							next[w, z, y, x] = '#'
						elif (space[w, z, y, x] == '#') and (neighbors == 3 or neighbors == 2):
							next[w, z, y, x] = '#'
		space = next.copy()
	return np.count_nonzero(space == '#')

def main():
	lst = list()
	with open("2020/day_17.in", "r") as f:
		for l in f:
			lst.append(np.array([c for c in l.split('\n')[0]]))
	mtx = np.array(lst)

	res1 = task1(mtx)
	print("Task 1: %d" % res1)

	res2 = task2(mtx)
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()