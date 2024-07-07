win_task1 = {
	"A": {"X": 3, "Y": 6, "Z": 0}, # rock
	"B": {"X": 0, "Y": 3, "Z": 6}, # paper
	"C": {"X": 6, "Y": 0, "Z": 3} # scisors
}
play_task1 = {"X": 1, "Y": 2, "Z": 3}

def task1(arr):
	score = 0
	for game in arr:
		p1, p2 = game.split(" ")
		score += play_task1[p2] + win_task1[p1][p2]
	return score

play_task2 = {
	"A": {"X": 3, "Y": 1, "Z": 2}, # rock
	"B": {"X": 1, "Y": 2, "Z": 3}, # paper
	"C": {"X": 2, "Y": 3, "Z": 1} # scisors
}
win_task2 = {"X": 0, "Y": 3, "Z": 6}

def task2(arr):
	score = 0
	for game in arr:
		p1, p2 = game.split(" ")
		score += play_task2[p1][p2] + win_task2[p2]
	return score

def main():
	arr = list()
	with open("2022/day_02.in", "r") as f:
		for l in f.readlines():
			arr.append(l.strip())

	print(f"Task 1: {task1(arr)}")
	print(f"Task 2: {task2(arr)}")


if __name__ == "__main__":
	main()