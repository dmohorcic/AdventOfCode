import numpy as np

def task1(crabs):
	min_score = np.inf
	min_pos = 0
	for pos in range(crabs.min(), crabs.max()+1):
		score = np.sum(np.abs(crabs-pos))
		if score < min_score:
			min_score = score
			min_pos = pos
	print(min_pos)
	return min_score

def score2(c):
	return int(np.sum((c*c+c)/2))

def task2(crabs):
	min_score = np.inf
	min_pos = 0
	for pos in range(crabs.min(), crabs.max()+1):
		score = np.sum(score2(np.abs(crabs-pos)))
		if score < min_score:
			min_score = score
			min_pos = pos
	print(min_pos)
	return min_score

if __name__ == "__main__":
	crabs = list()
	with open("2021/day_07.in", "r") as f:
		crabs = np.array([int(i) for i in f.readline().split("\n")[0].split(",")])

	print(task1(crabs))
	print(task2(crabs))