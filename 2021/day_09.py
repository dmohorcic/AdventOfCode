import numpy as np

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def isMinima(area, i, j):
	minimum = list()
	for d in directions:
		if i+d[0] < 0 or i+d[0] >= area.shape[0] or j+d[1] < 0 or j+d[1] >= area.shape[1]:
			minimum.append(True)
		else:
			minimum.append(area[i+d[0], j+d[1]] > area[i, j])
	return sum(minimum) == len(minimum)

def task1(area):
	low = 0
	dim = area.shape
	arr = list()
	for i in range(dim[0]):
		for j in range(dim[1]):
			if isMinima(area, i, j):
				low += area[i, j]+1
				arr.append((i, j))
	return low, arr

def getBasinSize(area, minima):
	size = 0 # from minima
	in_basin = list()
	possible_locations = [minima]
	while len(possible_locations) > 0:
		loc = possible_locations.pop(0)
		if loc[0] < 0 or loc[0] >= area.shape[0] or loc[1] < 0 or loc[1] >= area.shape[1]:
			continue
		if area[loc[0], loc[1]] < 9 and loc not in in_basin:
			in_basin.append(loc)
			size += 1
			possible_locations.append((loc[0]+1, loc[1]))
			possible_locations.append((loc[0]-1, loc[1]))
			possible_locations.append((loc[0], loc[1]+1))
			possible_locations.append((loc[0], loc[1]-1))
	return size

def task2(area, minima):
	basins = list()
	for low in minima:
		basins.append(getBasinSize(area, low))
	basins.sort(reverse=True)
	return basins[0]*basins[1]*basins[2]

if __name__ == "__main__":
	area = list()
	with open("2021/day_09.in", "r") as f:
		for i, l in enumerate(f.readlines()):
			tmp = l.split("\n")[0]
			area.append(np.array([int(k) for k in tmp]))
	area = np.array(area)
	
	risk, minima = task1(area)
	print(risk)
	print(task2(area, minima))