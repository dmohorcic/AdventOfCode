import numpy as np
import math

def task1(time, departs):
	best_ID, wait_time = 0, -1
	for d in departs:
		if d == 'x':
			continue
		d = int(d)
		k = time/d
		wait = d*math.ceil(k)-time
		if wait_time == -1 or wait < wait_time:
			wait_time = wait
			best_ID = d
	return wait_time*best_ID

def task2(departs):
	return 0

def main():
	with open("2020/day_13.in", "r") as f:
		time = int(f.readline()[:-1])
		departs = np.array(f.readline().split('\n')[0].split(','))
	
	res1 = task1(time, departs)
	print("Task 1: %d" % res1)

	res2 = task2(departs)
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()