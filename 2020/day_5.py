import numpy as np

def getSeatId(seat):
	row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
	col = int(seat[-3:].replace('L', '0').replace('R', '1'), 2)
	return row*8+col


def task1(arr):
	return max([getSeatId(seat) for seat in arr])

def task2(arr):
	ids = np.array([getSeatId(seat) for seat in arr])
	ids.sort()
	my_id = ids[0]
	for id in ids:
		if my_id != id:
			return my_id
		else:
			my_id += 1

def main():
	with open("2020/day_5.in") as f:
		lst = [l.split('\n')[0] for l in f]
	arr = np.array(lst)

	res1 = task1(arr)
	print("Task 1: %d" % res1)

	res2 = task2(arr)
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()