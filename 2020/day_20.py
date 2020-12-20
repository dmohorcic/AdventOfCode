import numpy as np

def isNeighbor(this, other):
	for e1 in this.values():
		for e2 in other.values():
			if (e1 == e2).all() or (e1[::-1] == e2).all():
				return True
	return False

def findNeighbors(edges):
	neighbors = dict()
	ids = list(edges.keys())
	for key in ids:
		neighbors[key] = list()

	for i in range(len(ids)):
		for j in range(i+1, len(ids)):
			if isNeighbor(edges[ids[i]], edges[ids[j]]):
				neighbors[ids[i]].append(j)
				neighbors[ids[j]].append(i)
	return neighbors

def task1(edges):
	neighbors = findNeighbors(edges)
	map_corner = list()
	map_edges = list()
	map_middle = list()
	for key, val in neighbors.items():
		if len(val) == 2:
			map_corner.append(key)
		elif len(val) == 3:
			map_edges.append(key)
		else:
			map_middle.append(key)
	s = int(1)
	for id in map_corner:
		s *= int(id)
	return s

def main():
	tiles = dict()
	edges = dict()
	with open("2020/day_20.in", "r") as f:
		while True:
			l = list()
			for i in range(11):
				l.append(f.readline().split('\n')[0])
			f.readline()
			if l[0] == '':
				break

			id = int(l[0].split(' ')[1].split(':')[0])
			grid = np.array([[c for c in x] for x in l[1:]])
			edge = dict()
			edge["l"] = grid[:, 0]
			edge["r"] = grid[:, 9]
			edge["u"] = grid[0, :]
			edge["d"] = grid[9, :]
			tiles[id] = grid
			edges[id] = edge
	
	res1 = task1(edges)
	print("Task 1: %d" % res1)

	res2 = task2(edges, tiles)
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()