import numpy as np

def task1(arr):
	print("Task 1")
	arr[1] = 12
	arr[2] = 2
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
	print(arr[0])

def task2(arr):
	print("Task 2")
	for i in range(100):
		for j in range(100):
			temp = arr.copy()
			temp[1] = i
			temp[2] = j
			idx = 0
			try:
				while True:
					ins = temp[idx]
					if ins == 99:
						break
					in1 = temp[idx+1]
					in2 = temp[idx+2]
					out = temp[idx+3]
					if ins == 1:
						temp[out] = temp[in1]+temp[in2]
					elif ins == 2:
						temp[out] = temp[in1]*temp[in2]
					else:
						raise Exception
					idx += 4
				if temp[0] == 19690720:
					print(100*temp[1]+temp[2])
					return
			except:
				continue

def main():
	lst = list()
	with open("2019/day_2.in", "r") as f:
		l = f.readline().split('\n')[0]
		lst = [int(s) for s in l.split(',')]
	arr = lst

	task1(arr.copy())
	task2(arr.copy())

if __name__ == "__main__":
	main()