import numpy as np

def determineLoopSize(public):
	subject_num = 7
	value = 1
	loop_size = 0
	while value != public:
		value *= subject_num
		value %= 20201227
		loop_size += 1
	return loop_size

def transform(subject_num, loop_size):
	value = 1
	for i in range(loop_size):
		value *= subject_num
		value %= 20201227
	return value

def task1(p_card, p_door):
	l_card = determineLoopSize(p_card)
	enc_key = transform(p_door, l_card)
	return enc_key

def main():
	with open("2020/day_25.in", "r") as f:
		public_card = int(f.readline().split('\n')[0])
		public_door = int(f.readline().split('\n')[0])

	res1 = task1(public_card, public_door)
	print("Task 1: %d" % res1)

if __name__ == "__main__":
	main()