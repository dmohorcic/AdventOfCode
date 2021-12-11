import numpy as np
from numpy.core.arrayprint import array_str

def task1(arr):
	most_common = np.round(arr.mean(axis=0)).astype("int")
	least_common = 1-most_common
	most_common = eval("0b"+"".join([str(i) for i in most_common]))
	least_common = eval("0b"+"".join([str(i) for i in least_common]))
	return most_common*least_common

def task2(arr):
	oxygen_list = arr.copy()
	for i in range(len(arr[0])):
		most_common = str(0 if np.mean([int(item[i]) for item in oxygen_list]) < 0.5 else 1)
		to_remove = list()
		for idx, item in enumerate(oxygen_list):
			if item[i] != most_common:
				to_remove.append(idx)
		for idx in to_remove[::-1]:
			oxygen_list.pop(idx)
		if len(oxygen_list) == 1:
			oxygen_list = oxygen_list[0]
			break

	dioxide_list = arr.copy()
	for i in range(len(arr[0])):
		least_common = str(1 if np.mean([int(item[i]) for item in dioxide_list]) < 0.5 else 0)
		to_remove = list()
		for idx, item in enumerate(dioxide_list):
			if item[i] != least_common:
				to_remove.append(idx)
		for idx in to_remove[::-1]:
			dioxide_list.pop(idx)
		if len(dioxide_list) == 1:
			dioxide_list = dioxide_list[0]
			break
	
	oxygen = eval("0b"+"".join([str(i) for i in oxygen_list]))
	dioxide = eval("0b"+"".join([str(i) for i in dioxide_list]))
	return oxygen*dioxide

if __name__ == "__main__":
	arr = list()
	with open("2021/day_03.in", "r") as f:
		for l in f.readlines():
			arr.append(l.split("\n")[0])
	tmp = np.zeros((len(arr), len(arr[0])))
	for i in range(len(arr)):
		tmp[i, :] = np.array([int(c) for c in arr[i]])

	print(f"Task 1: {task1(tmp)}")
	print(f"Task 2: {task2(arr)}")