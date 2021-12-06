import numpy as np

def task1(fish):
	for _ in range(80):
		l = len(fish)
		for idx in range(l):
			if fish[idx] == 0:
				fish[idx] = 6
				fish.append(8)
			else:
				fish[idx] -= 1
	return len(fish)

# track how many fish with certain clock there are
def task2(fish):
	fish = np.array(fish)
	clock = np.array([0 for _ in range(9)], dtype="int64")
	for i in range(9):
		clock[i] = np.sum(fish == i)
	
	for _ in range(256):
		next = np.array([0 for _ in range(9)], dtype="int64")
		for idx in range(8):
			next[idx] = clock[idx+1]
		next[8] = clock[0]
		next[6] += clock[0]
		clock = next

	return np.sum(clock)

if __name__ == "__main__":
	fish = list()
	with open("2021/day_06.in", "r") as f:
		fish = [int(i) for i in f.readline().split("\n")[0].split(",")]
	
	print(task1(fish.copy()))
	print(task2(fish.copy()))