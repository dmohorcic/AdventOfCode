import numpy as np

def task1(arr):
	print("Taks 1")
	print(sum(arr))

def task2(arr):
	print("Task 2")
	d = dict()
	f, i = 0, 0
	d[f] = 1
	while True:
		f += arr[i]
		i += 1
		if i == len(arr):
			i = 0
		if f in d.keys():
			print(f)
			return
		else:
			d[f] = 1

def main():
	lst = list()
	with open("2018/day_1.in", "r") as f:
		for l in f:
			lst.append(int(l.split('\n')[0]))
	arr = np.array(lst)

	task1(arr)
	task2(arr)

if __name__ == "__main__":
	main()