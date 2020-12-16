import numpy as np

def prepareRanges(rules):
	r = list()
	for val in rules.values():
		rang = val["low"].split('-')
		r.append(np.array([int(rang[0]), int(rang[1])]))
		rang = val["high"].split('-')
		r.append(np.array([int(rang[0]), int(rang[1])]))
	return r

def isValid(ticket, rules):
	error = 0
	for x in ticket:
		legal = False
		for rule in rules:
			if x >= rule[0] and x <= rule[1]:
				legal = True
				break
		if not legal:
			error += x
	if error == 0:
		return True, 0
	else:
		return False, error

def task1(rules, other):
	ranges = prepareRanges(rules)
	error = 0
	for ticket in other:
		valid, e = isValid(ticket, ranges)
		if not valid:
			error += e
	return error

def task2(rules, my, other):
	ranges = prepareRanges(rules)
	valid_tickets = list()
	for ticket in other:
		valid, e = isValid(ticket, ranges)
		if valid:
			valid_tickets.append(ticket)
	valid_tickets = np.array(valid_tickets)
	# todo
	return 0

def main():
	rules = dict()
	my = list()
	other = list()
	with open("2020/day_16.in", "r") as f:
		r = True
		m = False
		title = 0
		tmp = list()
		for l in f:
			if r:
				if l == '\n':
					r = False
					m = True
				else:
					args = l.split('\n')[0].split(": ")
					d = dict()
					d["low"] = args[1].split(" or ")[0]
					d["high"] = args[1].split(" or ")[1]
					rules[args[0]] = d
			elif m:
				if l == '\n':
					m = False
				else:
					if title == 0:
						title += 1
					else:
						my = np.array([int(x) for x in l.split('\n')[0].split(',')])
			else:
				if title == 1:
					title += 1
				else:
					tmp.append(np.array([int(x) for x in l.split('\n')[0].split(',')]))
		other = np.array(tmp)
	
	res1 = task1(rules, other)
	print("Task 1: %d" % res1)

	res2 = task2(rules, my, other)
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()