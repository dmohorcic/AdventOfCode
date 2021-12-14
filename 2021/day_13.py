def arrInList(arr, lst):
	for l in lst:
		if arr[0] == l[0] and arr[1] == l[1]:
			return True
	return False

def printCode(chars):
	max_x = max([i[0] for i in chars])+1
	max_y = max([i[1] for i in chars])+1
	img = [[" " for _ in range(max_x)] for _ in range(max_y)]
	for c in chars:
		img[c[1]][c[0]] = "#"
	for line in img:
		for l in line:
			print(l, end="")
		print("")

def task1(chars, folds):
	fold = folds[0]
	fold_along = fold[1]
	new_chars = list()
	if fold[0] == "x":
		for c in chars:
			if c[0] < fold_along:
				new_c = c.copy()
			else:
				new_c = c.copy()
				new_c[0] = -new_c[0]+2*fold_along
			if not arrInList(new_c, new_chars):
				new_chars.append(new_c)
	else:
		for c in chars:
			if c[1] < fold_along:
				new_c = c.copy()
			else:
				new_c = c.copy()
				new_c[1] = -new_c[1]+2*fold_along
			if not arrInList(new_c, new_chars):
				new_chars.append(new_c)
	return len(new_chars)

def task2(chars, folds):
	for fold in folds:
		fold_along = fold[1]
		new_chars = list()
		if fold[0] == "x":
			for c in chars:
				if c[0] < fold_along:
					new_c = c.copy()
				else:
					new_c = c.copy()
					new_c[0] = -new_c[0]+2*fold_along
				if not arrInList(new_c, new_chars):
					new_chars.append(new_c)
		else:
			for c in chars:
				if c[1] < fold_along:
					new_c = c.copy()
				else:
					new_c = c.copy()
					new_c[1] = -new_c[1]+2*fold_along
				if not arrInList(new_c, new_chars):
					new_chars.append(new_c)
		chars = new_chars
	
	printCode(chars)

if __name__ == "__main__":
	chars = list()
	folds = list()
	with open("2021/day_13.in", "r") as f:
		l = f.readline()
		while l != "\n":
			tmp = l.split("\n")[0].split(",")
			chars.append([int(i) for i in tmp])
			l = f.readline()
		
		for l in f.readlines():
			tmp = l.split("\n")[0][11:].split("=")
			folds.append((tmp[0], int(tmp[1])))
	
	print(f"Task 1: {task1(chars, folds)}")
	print(f"Task 2:")
	task2(chars, folds)