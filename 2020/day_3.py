import numpy as np

def traverse(mtx, x_slope, y_slope):
	s = 0
	x = x_slope
	y = y_slope
	while y < len(mtx):
		if mtx[y, x] == '#':
			s += 1
		x += x_slope
		y += y_slope
		if x >= len(mtx[0]):
			x -= len(mtx[0])
	return s


def task1(mtx):
	return traverse(mtx, 3, 1)

def task2(mtx):
	s1 = traverse(mtx, 1, 1)
	s2 = traverse(mtx, 3, 1)
	s3 = traverse(mtx, 5, 1)
	s4 = traverse(mtx, 7, 1)
	s5 = traverse(mtx, 1, 2)
	return s1*s2*s3*s4*s5

def main():
	lst = list()
	with open("2020/day_3.in", "r") as f:
		for l in f:
			l = l.split('\n')[0]
			row = [c for c in l]
			lst.append(row)
	mtx = np.array(lst)
	
	res1 = task1(mtx)
	print("Task 1: %d\n" % res1)

	res2 = task2(mtx)
	print("Task 2: %d\n" % res2)

if __name__ == "__main__":
	main()