def task1(d):
	correct = 0
	for val in d.values():
		correct += len(val)
	return correct

def task2(d):
	correct = 0
	for val in d.values():
		if len(val) == 1:
			correct += len(val[0])
		else:
			for ans in val[0]:
				in_all = True
				for i in range(1, len(val)):
					if ans not in val[i]:
						in_all = False
						break
				if in_all:
					correct += 1
	return correct

def main():
	d = dict()
	with open("2020/day_6.in") as f:
		s = set()
		i = 0
		for l in f:
			if l == '\n':
				d[i] = s
				s = set()
				i += 1
			else:
				for char in l:
					if char == '\n':
						break
					s.add(char)
		d[i] = s

	res1 = task1(d)
	print("Task 1: %d" % res1)

	d = dict()
	with open("2020/day_6.in") as f:
		lst = list()
		i = 0
		for l in f:
			if l == '\n':
				d[i] = lst
				lst = list()
				i += 1
			else:
				tmp = list()
				for char in l:
					if char == '\n':
						break
					tmp.append(char)
				lst.append(tmp)
		d[i] = lst

	res2 = task2(d)
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()