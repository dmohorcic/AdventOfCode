import numpy as np

def task1(lst):
	print("Task 1")
	valid = 0
	for val in lst.values():
		c = val["pass"].count(val["char"])
		if c <= val["high"] and c >= val["low"]:
			valid += 1
	print(valid)

def task2(lst):
	print("Task 2")
	valid = 0
	for val in lst.values():
		left = val["pass"][val["low"]-1] == val["char"]
		right = val["pass"][val["high"]-1] == val["char"]
		if left and not right or not left and right:
			valid += 1
	print(valid)

def main():
	lst = dict()
	i = 0
	with open("2020/day_2.in", "r") as f:
		for l in f:
			args = l.split(": ")
			d = dict()
			d["pass"] = args[1]
			args = args[0].split(' ')
			d["char"] = args[1]
			args = args[0].split('-')
			d["low"] = int(args[0])
			d["high"] = int(args[1])
			lst[str(i)] = d
			i += 1

	task1(lst)
	task2(lst)

if __name__ == "__main__":
	main()