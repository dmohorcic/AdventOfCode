import numpy as np

def sumExists(arr, idx):
	for i in range(idx-25, idx):
		for j in range(i+1, idx):
			if arr[i]+arr[j] == arr[idx]:
				return True
	return False

def task1(arr):
	for i in range(25, len(arr)):
		if not sumExists(arr, i):
			return arr[i]

def task2(arr):
	for i in range(25, len(arr)):
		if not sumExists(arr, i):
			idx = i
			break
	for i in range(idx):
		s = arr[i]
		for j in range(i+1, idx):
			s += arr[j]
			if s > arr[idx]:
				break
			if s == arr[idx]:
				return arr[i]+arr[j]

def main():
	lst = list()
	with open("2020/day_9.in") as f:
		for l in f:
			lst.append(int(l.split(' ')[0]))
	arr = np.array(lst)

	res1 = task1(arr)
	print("Task 1: %d" % res1)

	res2 = task2(arr)
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()