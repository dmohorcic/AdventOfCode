import numpy as np

def task1(arr):
	print("Task 1")
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if arr[i]+arr[j] == 2020:
				print(arr[i]*arr[j])
				return

def task2(arr):
	print("Task 2")
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			for k in range(j+1, len(arr)):
				if arr[i]+arr[j]+arr[k] == 2020:
					print(arr[i]*arr[j]*arr[k])
					return

def main():
	lst = list()
	with open("day_1.txt", "r") as f:
		for l in f:
			lst.append(int(l.split('\n')[0]))
	arr = np.array(lst)

	task1(arr)
	task2(arr)

if __name__ == "__main__":
	main()