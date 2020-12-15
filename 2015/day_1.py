def task1(arr):
	floor = 0
	for c in arr:
		if c == '(':
			floor += 1
		else:
			floor -= 1
	return floor

def task2(arr):
	floor = 0
	i = 1
	for c in arr:
		if c == '(':
			floor += 1
		else:
			floor -= 1
		if floor == -1:
			return i
		i += 1

def main():
	with open("2015/day_1.in", "r") as f:
		arr = f.readline().split('\n')[0]
	
	res1 = task1(arr)
	print("Task 1: %d" % res1)

	res2 = task2(arr)
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()