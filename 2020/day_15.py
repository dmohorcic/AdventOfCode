def prepareDict(lst):
	d = dict()
	for i in range(len(lst)-1):
		d[lst[i]] = i
	return d

def simulate(lst, ith):
	d = prepareDict(lst)
	last_spoken = lst[-1]
	for i in range(len(lst), ith):
		if last_spoken in d.keys():
			next_spoken = i-d[last_spoken]-1
			d[last_spoken] = i-1
			last_spoken = next_spoken
		else:
			d[last_spoken] = i-1
			last_spoken = 0
	return last_spoken

def task1(lst):
	return simulate(lst, 2020)

def task2(lst):
	return simulate(lst, 30000000)

def main():
	lst = list()
	with open("2020/day_15.in", "r") as f:
		lst = [int(x) for x in f.readline().split('\n')[0].split(',')]
	
	res1 = task1(lst)
	print("Task 1: %d" % res1)

	res2 = task2(lst)
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()