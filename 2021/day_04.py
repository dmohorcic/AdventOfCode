import re
import numpy as np

def hasWon(board):
	return np.sum(-5 == np.sum(board, axis=0)) > 0 or np.sum(-5 == np.sum(board, axis=1)) > 0

def task1(seq, boards):
	fastest = len(seq)
	score = 0
	for board in boards:
		for i, t in enumerate(seq):
			idx = np.where(board == t)
			if idx[0].shape[0] == 1:
				board[idx[0][0], idx[1][0]] = -1
			if hasWon(board):
				if i < fastest:
					fastest = i
					board[np.where(board == -1)] = 0
					score = np.sum(board)*t
				break
	return int(score)

def task2(seq, boards):
	slowest = 0
	score = 0
	for board in boards:
		for i, t in enumerate(seq):
			idx = np.where(board == t)
			if idx[0].shape[0] == 1:
				board[idx[0][0], idx[1][0]] = -1
			if hasWon(board):
				if i > slowest:
					slowest = i
					board[np.where(board == -1)] = 0
					score = np.sum(board)*t
				break
	return int(score)

if __name__ == "__main__":
	seq = list()
	boards = list()
	with open("2021/day_04.in", "r") as f:
		seq = f.readline().split("\n")[0].split(",")
		seq = [int(i) for i in seq]
		f.readline()
	
		board = np.zeros((5, 5))
		i = 0
		for line in f.readlines():
			if line == "\n":
				boards.append(board)
				board = np.zeros((5, 5))
				i = 0
			else:
				tmp = re.sub("^ +", "", re.sub(" +", " ", line.split("\n")[0])).split(" ")
				board[i, :] = np.array([int(c) for c in tmp])
				i += 1
		boards.append(board)
	
	print(f"Task 1: {task1(seq, [board.copy() for board in boards])}")
	print(f"Task 2: {task2(seq, boards)}")