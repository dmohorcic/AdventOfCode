def task1(lines):
	coords = dict()
	c = (0, 0)
	for i in lines[0]:
		d = i[0]
		l = int(i[1:])
		if d == 'U':
			for j in range(c[1]+1, c[1]+l+1):
				coords[(c[0], j)] = True
			c = (c[0], c[1]+l)
		elif d == 'D':
			for j in range(c[1]-l, c[1]):
				coords[(c[0], j)] = True
			c = (c[0], c[1]-l)
		elif d == 'R':
			for j in range(c[0]+1, c[0]+l+1):
				coords[(j, c[1])] = True
			c = (c[0]+l, c[1])
		elif d == 'L':
			for j in range(c[0]-l, c[0]):
				coords[(j, c[1])] = True
			c = (c[0]-l, c[1])
	
	closest_dist = float('inf')
	c = (0, 0)
	for i in lines[1]:
		d = i[0]
		l = int(i[1:])
		if d == 'U':
			for j in range(c[1]+1, c[1]+l+1):
				if (c[0], j) in coords and abs(c[0])+abs(j) < closest_dist:
					closest_dist = abs(c[0])+abs(j)
			c = (c[0], c[1]+l)
		elif d == 'D':
			for j in range(c[1]-1, c[1]-l-1, -1):
				if (c[0], j) in coords and abs(c[0])+abs(j) < closest_dist:
					closest_dist = abs(c[0])+abs(j)
			c = (c[0], c[1]-l)
		elif d == 'R':
			for j in range(c[0]+1, c[0]+l+1):
				if (j, c[1]) in coords and abs(c[1])+abs(j) < closest_dist:
					closest_dist = abs(c[1])+abs(j)
			c = (c[0]+l, c[1])
		elif d == 'L':
			for j in range(c[0]-1, c[0]-l-1, -1):
				if (j, c[1]) in coords and abs(c[1])+abs(j) < closest_dist:
					closest_dist = abs(c[1])+abs(j)
			c = (c[0]-l, c[1])
	return closest_dist

def task2(lines):
	coords = dict()
	c = (0, 0)
	step = 1
	for i in lines[0]:
		d = i[0]
		l = int(i[1:])
		if d == 'U':
			for j in range(c[1]+1, c[1]+l+1):
				coords[(c[0], j)] = step
				step += 1
			c = (c[0], c[1]+l)
		elif d == 'D':
			for j in range(c[1]-1, c[1]-l-1, -1):
				coords[(c[0], j)] = step
				step += 1
			c = (c[0], c[1]-l)
		elif d == 'R':
			for j in range(c[0]+1, c[0]+l+1):
				coords[(j, c[1])] = step
				step += 1
			c = (c[0]+l, c[1])
		elif d == 'L':
			for j in range(c[0]-1, c[0]-l-1, -1):
				coords[(j, c[1])] = step
				step += 1
			c = (c[0]-l, c[1])
	
	closest_steps = float('inf')
	c = (0, 0)
	step = 1
	for i in lines[1]:
		d = i[0]
		l = int(i[1:])
		if d == 'U':
			for j in range(c[1]+1, c[1]+l+1):
				if (c[0], j) in coords and coords[(c[0], j)]+step < closest_steps:
					closest_steps = coords[(c[0], j)]+step
				step += 1
			c = (c[0], c[1]+l)
		elif d == 'D':
			for j in range(c[1]-1, c[1]-l-1, -1):
				if (c[0], j) in coords and coords[(c[0], j)]+step < closest_steps:
					closest_steps = coords[(c[0], j)]+step
				step += 1
			c = (c[0], c[1]-l)
		elif d == 'R':
			for j in range(c[0]+1, c[0]+l+1):
				if (j, c[1]) in coords and coords[(j, c[1])]+step < closest_steps:
					closest_steps = coords[(j, c[1])]+step
				step += 1
			c = (c[0]+l, c[1])
		elif d == 'L':
			for j in range(c[0]-1, c[0]-l-1, -1):
				if (j, c[1]) in coords and coords[(j, c[1])]+step < closest_steps:
					closest_steps = coords[(j, c[1])]+step
				step += 1
			c = (c[0]-l, c[1])
	return closest_steps

def main():
	lines = list()
	with open("2019/day_3.in", "r") as f:
		for l in f:
			l = l.split('\n')[0]
			lines.append(l.split(','))

	res1 = task1(lines)
	print("Task 1: %d" % res1)

	res2 = task2(lines)
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()