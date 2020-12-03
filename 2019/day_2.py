import numpy as np

def simulate(arr, arg1, arg2):
	arr[1] = arg1
	arr[2] = arg2
	i = 0
	while True:
		ins = arr[i]
		if ins == 99:
			break
		in1 = arr[i+1]
		in2 = arr[i+2]
		out = arr[i+3]
		if ins == 1:
			arr[out] = arr[in1]+arr[in2]
		elif ins == 2:
			arr[out] = arr[in1]*arr[in2]
		i += 4

def task1(arr):
	simulate(arr, 12, 2)
	return arr[0]

def task2(arr):
	for i in range(100):
		for j in range(100):
			temp = arr.copy()
			try:
				simulate(temp, i, j)
				if temp[0] == 19690720:
					return 100*temp[1]+temp[2]
			except:
				continue

def main():
	lst = list()
	with open("2019/day_2.in", "r") as f:
		l = f.readline().split('\n')[0]
		lst = [int(s) for s in l.split(',')]
	arr = lst

	res1 = task1(arr.copy())
	print("Task 1: %d" % res1)

	res2 = task2(arr.copy())
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()