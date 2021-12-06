def task1(arr):
	horizontal = 0
	depth = 0
	for move in arr:
		if move[0] == "forward":
			horizontal += int(move[1])
		elif move[0] == "down":
			depth += int(move[1])
		else:
			depth -= int(move[1])
	return horizontal*depth

def task2(arr):
	horizontal = 0
	depth = 0
	aim = 0
	for move in arr:
		if move[0] == "forward":
			horizontal += int(move[1])
			depth += aim*int(move[1])
		elif move[0] == "down":
			aim += int(move[1])
		else:
			aim -= int(move[1])
	return horizontal*depth

if __name__ == "__main__":
	arr = list()
	with open("2021/day_2.in", "r") as f:
		for l in f.readlines():
			arr.append(l.split("\n")[0].split(" "))

	print(task1(arr))
	print(task2(arr))