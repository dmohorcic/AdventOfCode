def simulate(arr, times):
	i = 0
	for c in range(times):
		current = arr[i]
		
		# choose next 3
		next = list()
		t = 0
		i += 1
		while t < 3:
			if i < len(arr):
				next.append(arr.pop(i))
				t += 1
			else:
				i = 0
		
		# find destination
		dest = current-1
		while True:
			if dest == 0:
				dest = len(arr)+3
			if dest in arr:
				idx = arr.index(dest)
				break
			dest -= 1

		# put back picked up
		arr.insert(idx+1, next[2])
		arr.insert(idx+1, next[1])
		arr.insert(idx+1, next[0])

		# next curretn
		i = arr.index(current)+1
		if i >= len(arr):
			i -= len(arr)
	return arr

def sim(rel, times, first):
	prev = first
	for c in range(times):
		current = prev

		unmoved = [rel[current]]
		for i in range(2):
			unmoved.append(rel[unmoved[-1]])
		
		target = current-1
		while target in unmoved:
			if target == 0:
				target = len(rel.keys())
			else:
				target -= 1
		if target == 0:
			target = len(rel.keys())
		
		rel[current] = rel[unmoved[2]]
		nxt = rel[target]
		rel[target] = unmoved[0]
		rel[unmoved[2]] = nxt

		prev = rel[current]

def task1(arr):
	simulate(arr, 100)
	
	s = ""
	i = arr.index(1)+1
	for l in range(len(arr)-1):
		if i >= len(arr):
			i -= len(arr)
		s += str(arr[i])
		i += 1
	return s

def task2(arr):
	relations = dict()
	for i in range(len(arr)-1):
		relations[arr[i]] = arr[i+1]
	relations[arr[len(arr)-1]] = 10
	for i in range(10, 1000000):
		relations[i] = i+1
	relations[1000000] = arr[0]
	
	sim(relations, 10000000, arr[0])

	nxt = relations[1]
	return int(relations[nxt])*int(nxt)

def main():
	lst = list()
	with open("2020/day_23.in", "r") as f:
		lst = [int(c) for c in f.readline().split('\n')[0]]
	
	res1 = task1(lst.copy())
	print("Task 1: %s" % res1)

	res2 = task2(lst.copy())
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()