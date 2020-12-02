import numpy as np
import math

def task1(arr):
	print("Task 1")
	print(sum([math.floor(x/3)-2 for x in arr]))


def task2(arr):
	print("Task 2")
	s = 0
	for x in arr:
		fuel = math.floor(x/3)-2
		additional_fuel = math.floor(fuel/3)-2
		while additional_fuel > 0:
			fuel += additional_fuel
			additional_fuel = math.floor(additional_fuel/3)-2
		s += fuel
	print(s)


def main():
	lst = list()
	with open("2019/day_1.in", "r") as f:
		for l in f:
			lst.append(int(l.split('\n')[0]))
	arr = np.array(lst)
	
	task1(arr)
	task2(arr)

if __name__ == "__main__":
	main()