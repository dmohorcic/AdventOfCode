def task1(arr):
	increases = 0
	for i in range(1, len(arr)):
		if arr[i] > arr[i-1]:
			increases += 1
	return increases

def task2(arr):
	increases = 0
	for i in range(4, len(arr)+1):
		prev = sum(arr[i-4:i-1])
		next = sum(arr[i-3:i])
		if next > prev:
			increases += 1
	return increases

if __name__ == "__main__":
	arr = list()
	with open("2021/day_01.in", "r") as f:
		for l in f.readlines():
			arr.append(int(l))

	print(f"Task 1: {task1(arr)}")
	print(f"Task 1: {task2(arr)}")